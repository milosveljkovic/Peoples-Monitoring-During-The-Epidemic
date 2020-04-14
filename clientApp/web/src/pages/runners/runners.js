import React from 'react';
import {
    ENDPOINT_URL
} from '../../common/constants'
import {getRunnersService} from '../../services.js/runner.service'

class Runners extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            runners:[]
        }
    }

    getRunners=()=>{
        getRunnersService().then(res=>{
            this.setState({runners:res.data})
        })
    }

    render() {
        return (
            <div className={'container'}>
                <div style={{textAlign:'center',margin:'30px'}}>
                    <h3 style={{opacity:'0.6'}}>
                        List of runners
                    </h3>
                </div>
                <div style={{textAlign:'center',margin:'30px'}}>
                    {this.state.runners.length===0 &&
                    <button className={"btn btn-primary"} 
                    onClick={this.getRunners}
                    >Get Runners</button>}
                    <div style={{height:'300px',overflow:'auto'}}>
                    {
                        this.state.runners.length!==0 &&
                        this.state.runners.map(runner=>{
                            return <p  key={runner.id}>{runner.id}</p>
                        })
                    }
                    </div>
                </div>
            </div>
        )
    }
}

export default Runners;