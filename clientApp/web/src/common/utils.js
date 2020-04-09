
export function generateRequest(method, url) {
    return {
        method: method,
        url: `${url}`,
        headers: {
            'Content-Type':'application/json'
        }
    }
}