import type { ChangeEvent, FormEvent, ReactElement } from 'react'
import { useEffect, useState } from 'react'

import { baseUrl } from '../../configuration'
import { getCookie } from '../../utils/get-cookie'
import type { IFileInterface } from './index-interfaces'


export function Index(): ReactElement {
    const [selectedFile, setSelectedFile] = useState<File | null>(null)
    const [filesData, setFilesData] = useState<IFileInterface[]>([])
    const [openFiles, setOpenFiles] = useState<Record<number, boolean>>({})

    useEffect(
        () => {
            async function fetchFiles() {
                const url = `${baseUrl}/files/`
                const response = await fetch(
                    url,
                    {
                        method: 'GET',
                        credentials: 'include'
                    }
                )
                setFilesData(await response.json())
            }

            fetchFiles()
        }, []
    )

    function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
        const file = event.target.files?.[0] || null
        setSelectedFile(file)
    }

    async function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()

        const csrfToken = getCookie('csrftoken')

        if (selectedFile && csrfToken) {
            const url = `${baseUrl}/files/`
            const formData = new FormData()

            formData.append('file', selectedFile)

            const response = await fetch(
                url,
                {
                    method: 'POST',
                    credentials: 'include',
                    headers: {'X-CSRFToken': csrfToken},
                    body: formData,
                }
            )

            const uploadedFile = await response.json()

            setFilesData([...filesData, uploadedFile])
        }
    }

    function toggleFile(id: number) {
        setOpenFiles(prev => ({
            ...prev,
            [id]: !prev[id],
        }))
    }

    async function handleReplace(id: number, event: ChangeEvent<HTMLInputElement>) {
        const selectedFile = event.target.files?.[0] || null
        const url = `${baseUrl}/files/${id}/`
        const csrfToken = getCookie('csrftoken')
        

        if (selectedFile && csrfToken) {
            const formData = new FormData()
            formData.append('file', selectedFile)

            const response = await fetch(
                url,
                {
                    method: 'PATCH',
                    credentials: 'include',
                    headers: {'X-CSRFToken': csrfToken},
                    body: formData,
                }
            )

            const updatedFile = await response.json()

            setFilesData(current =>
                current.map(file =>
                    file.id === updatedFile.id
                        ? { ...file, ...updatedFile }
                        : file
                )
            )
        }
    }

    async function handleDelete(id: number) {
        const url = `${baseUrl}/files/${id}/`
        const csrfToken = getCookie('csrftoken')

        if (csrfToken) {
            await fetch(
                url,
                    {
                    method: 'DELETE',
                    credentials: 'include',
                    headers: {'X-CSRFToken': csrfToken},
                }
            )

            setFilesData(prev => prev.filter(file => file.id !== id))
            setOpenFiles(prev => {
                const copy = { ...prev }
                delete copy[id]
                return copy
            })
        }
    }

    return (
        <div className='flex flex-col items-center pt-20 w-full'>
            <form className='w-full max-w-lg space-y-4 p-8' onSubmit={handleSubmit}>
                <div className='space-y-2'>
                    <div className='flex items-center border border-gray-300 rounded-xl px-4 py-2'>
                        <span className='text-gray-500 flex-grow'>
                            {selectedFile ? selectedFile.name : 'Choose a file...'}
                        </span>

                        <input
                            id='file'
                            type='file'
                            className='hidden'
                            onChange={handleChange}
                        />

                        <label
                            htmlFor='file'
                            className='py-2 px-4 rounded-xl bg-gray-700 text-white font-medium hover:bg-gray-800 cursor-pointer'
                        >
                            Choose file
                        </label>
                    </div>
                </div>

                <button
                    type='submit'
                    className='py-2 px-8 rounded-xl bg-gray-700 text-white font-medium hover:bg-gray-800 cursor-pointer mx-auto block'
                >
                    Upload
                </button>
            </form>

            <div className='w-full max-w-2xl mt-10 space-y-4'>
                {filesData?.map(file => (
                    <div
                        key={file.id}
                        className='border border-gray-300 rounded-xl p-4 cursor-pointer hover:bg-gray-50 transition'
                        onClick={() => toggleFile(file.id)}
                    >
                        <div className='flex justify-between items-center'>
                            <div className='flex flex-col'>
                                <span className='font-medium text-gray-700'>
                                    File: {file.file}
                                </span>

                                <span className='text-sm text-gray-500'>
                                    Last status: {file.last_check_status}
                                </span>

                                <span className='text-sm text-gray-500'>
                                    Checked at: {file.last_checked_at}
                                </span>
                            </div>

                            <div className='flex items-center space-x-2' onClick={e => e.stopPropagation()}>
                                <label
                                    htmlFor={`edit-file-${file.id}`}
                                    className='p-2 rounded-lg hover:bg-gray-200 cursor-pointer text-xl'
                                >
                                    ✏️
                                </label>

                                <input
                                    id={`edit-file-${file.id}`}
                                    type='file'
                                    className='hidden'
                                    onChange={e => handleReplace(file.id, e)}
                                />

                                <button
                                    onClick={() => handleDelete(file.id)}
                                    className='p-2 rounded-lg hover:bg-red-100 cursor-pointer text-xl'
                                >
                                    🗑️
                                </button>
                            </div>
                        </div>

                        {openFiles[file.id] && (
                            <div className='mt-4 border-t border-gray-200 pt-4 space-y-3'>
                                {file.checks.length === 0 && (
                                    <div className='text-sm text-gray-500'>No checks yet.</div>
                                )}

                                {file.checks.map((check, i) => (
                                    <div
                                        key={i}
                                        className='border border-gray-200 rounded-lg p-3 bg-gray-50'
                                    >
                                        <div className='text-sm'>
                                            <span className='font-medium text-gray-700'>Status:</span> {check.status}
                                        </div>

                                        <div className='text-sm'>
                                            <span className='font-medium text-gray-700'>Datetime:</span> {check.datetime}
                                        </div>

                                        <div className='text-sm font-mono'>
                                            <span className='font-semibold'>Results:</span>
                                            <span className='whitespace-pre-wrap'> {check.results}</span>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                ))}
            </div>
        </div>
    )
}
