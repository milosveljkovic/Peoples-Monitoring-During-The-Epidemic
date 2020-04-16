import {generateRequest} from '../common/utils'
import {METHOD} from '../common/constants'
import axios from 'axios';

export function testRequest(user) {
    const options={
        data:user
    }
    var config = generateRequest(METHOD.POST, 'set_user',options);
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}

export function getRunnersService() {
    var config = generateRequest(METHOD.GET, 'get_user',{});
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}

export function getRunnerService(runner_id) {
    var config = generateRequest(METHOD.GET, `runner/${runner_id}`,{});
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}

export function getRunnerPathService(runner_id) {
    var config = generateRequest(METHOD.GET, `path?runner_id=${runner_id}`,{});
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}