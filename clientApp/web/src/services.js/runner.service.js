import {generateRunnerRequest,generatePathRequest} from '../common/utils'
import {METHOD} from '../common/constants'
import axios from 'axios';

export function testRequest(user) {
    const options={
        data:user
    }
    var config = generateRunnerRequest(METHOD.POST, 'api/runner/set_runner',options);
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}

export function getRunnersService() {
    var config = generateRunnerRequest(METHOD.GET, 'api/runner/get_runners',{});
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}

export function getRunnerService(runner_id) {
    var config = generateRunnerRequest(METHOD.GET, `api/runner/${runner_id}`,{});
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}

export function getRunnerPathService(runner_id) {
    var config = generatePathRequest(METHOD.GET, `api/path?runner_id=${runner_id}`,{});
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}

export function savePathService(path){
    const options={
        data:path
    }
    var config = generatePathRequest(METHOD.POST, 'api/path/set_path',options);
    return axios(config)
        .then(response => response)
        .catch(errorMessage =>errorMessage)
}