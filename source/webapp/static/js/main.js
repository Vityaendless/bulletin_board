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

async function onSubmitForExit(e) {
    e.preventDefault();
    console.log(e.target);
    try {
        let response = await makeRequest(
            'http://127.0.0.1:8000/api/v1/logout/',
            "POST",
            {},
            localStorage.getItem('apiToken')
        );
        localStorage.removeItem('apiToken');
        console.log(response);
    } finally {
        e.target.submit();
    }
}

async function onLoadForExit() {
    let logoutForm = document.getElementById('logout-form');
    if(logoutForm) {
        logoutForm.addEventListener('submit', onSubmitForExit);
    }
}

window.addEventListener('load', onLoadForExit);
