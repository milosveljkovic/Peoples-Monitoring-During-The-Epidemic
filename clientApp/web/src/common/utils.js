import {ENDPOINT_URL} from './constants'
export function generateRequest(method, url,options) {
    return {
        method: method,
        url: `${ENDPOINT_URL}${url}`,
        headers: {
            'Content-Type':'application/json'
        },
        ...options
    }
}