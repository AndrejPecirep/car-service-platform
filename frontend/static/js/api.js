const API_BASE = "/api"

async function apiRequest(endpoint, method = "GET", data = null) {

    const options = {
        method: method,
        headers: {
            "Content-Type": "application/json"
        }
    }

    if (data) {
        options.body = JSON.stringify(data)
    }

    const response = await fetch(API_BASE + endpoint, options)

    if (!response.ok) {
        const text = await response.text()
        throw new Error(text)
    }

    return await response.json()
}