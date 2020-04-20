import {RUNNER_ENDPOINT_URL,PATH_ENDPOINT_URL} from './constants'

export function generateRunnerRequest(method, url,options) {
    return {
        method: method,
        url: `${RUNNER_ENDPOINT_URL}${url}`,
        headers: {
            'Content-Type':'application/json'
        },
        ...options
    }
}

export function generatePathRequest(method, url,options) {
    return {
        method: method,
        url: `${PATH_ENDPOINT_URL}${url}`,
        headers: {
            'Content-Type':'application/json'
        },
        ...options
    }
}