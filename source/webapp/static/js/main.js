async function makeRequest(url, method='GET', data=null, token=null) {
    let headers = {
        "Content-Type": "application/json"
    };
    if (token) {
        headers['Authorization'] = 'Token ' + token;
    }

    let options;

    if (method !== "GET") {
        options = {method, headers, body: JSON.stringify(data)};
    } else {
        options = {method, headers};
    }

    let response = await fetch(url, options);

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function onLoad() {
    console.log("response");
}

window.addEventListener('load', onLoad);
