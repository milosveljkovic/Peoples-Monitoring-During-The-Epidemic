import {generateRequest} from '../common/utils'
import {METHOD} from '../common/constants'
import axios from 'axios';

export function testRequest(user) {
    const options={
        data:user
    }
    var config = generateRequest(METHOD.POST, 'api/runner/set_runner',options);
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}

export function getRunnersService() {
    var config = generateRequest(METHOD.GET, 'api/runner/get_runner',{});
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}

export function getRunnerService(runner_id) {
    var config = generateRequest(METHOD.GET, `api/runner/${runner_id}`,{});
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}

export function getRunnerPathService(runner_id) {
    var config = generateRequest(METHOD.GET, `api/path?runner_id=${runner_id}`,{});
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}