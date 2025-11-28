export interface IFileInterface {
    id: number
    file: string
    last_checked_at: string
    last_check_status: string
    checks: Array<{
        status: string
        datetime: string
        results: string
        email_sent: boolean
    }>
}
