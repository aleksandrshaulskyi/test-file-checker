const onLocalhost = window.location.hostname == 'localhost'

export const baseUrl = onLocalhost? 'http://localhost/api' : 'http://shaulskyi.com/api'
