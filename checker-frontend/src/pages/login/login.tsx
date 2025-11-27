







import type { ChangeEvent, FormEvent, ReactElement } from 'react'
import { useState } from 'react'

import { useNavigate } from 'react-router-dom'

import { baseUrl } from '../../configuration'


export function Login(): ReactElement {
    const navigate = useNavigate()

    const [loginForm, setLoginForm] = useState<Record<string, string> | null>(null)

    function handleChange(event: ChangeEvent<HTMLInputElement>) {
        const element = event.target

        setLoginForm(
            current => (
                {
                    ...current,
                    [element.id]: element.value,
                }
            )
        )
    }

    async function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()

        const url = `${baseUrl}/login/`

        await fetch(
            url,
            {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                credentials: 'include',
                body: JSON.stringify(loginForm),
            }
        )

        navigate('/')
    }

    return (
        <div className='flex items-center justify-center min-h-screen'>
            <div className='flex items-center justify-center min-h-screen'>
                <form className='w-full max-w-xl space-y-4 p-8 rounded-xl border border-gray-200 bg-white' onSubmit={handleSubmit}>
                    <h1 className='text-2xl font-medium text-gray-700 text-center'>
                        Login
                    </h1>
                    <div className='space-y-2'>
                        <label
                            htmlFor='email'
                            className='block text-sm font-medium text-gray-700'
                        >
                            Email
                        </label>
                        <input
                            id='email'
                            type='email'
                            placeholder='Enter email'
                            className='w-full rounded-xl border border-gray-300 px-4 py-2 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400'
                            onChange={handleChange}
                        />
                    </div>

                    <div className='space-y-2'>
                        <label
                            htmlFor='password'
                            className='block text-sm font-medium text-gray-700'
                        >
                            Password
                        </label>
                        <input
                            id='password'
                            type='password'
                            placeholder='Enter password'
                            className='w-full rounded-xl border border-gray-300 px-4 py-2 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400'
                            onChange={handleChange}
                        />
                    </div>

                    <button
                        type='submit'
                        className='py-2 px-8 rounded-xl bg-gray-700 text-white font-medium hover:bg-gray-800 cursor-pointer mx-auto block'
                    >
                        Login
                    </button>
                </form>
            </div>
        </div>
    )
}
