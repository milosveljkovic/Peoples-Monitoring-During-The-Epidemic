import {generateRequest} from '../common/utils'
import {METHOD, ENDPOINT_URL} from '../common/constants'
import axios from 'axios';

export function testRequest() {

    var config = generateRequest(METHOD.GET, '/time');
    return axios(config)
        .then(response => response)
        .catch((errorMessage) => {
            console.log(errorMessage)
        });
}