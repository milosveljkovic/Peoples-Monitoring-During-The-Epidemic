import React from 'react';
import {getRunnersService,getRunnerService,getRunnerPathService} from '../../services.js/runner.service'
import './runners.css'

class Runners extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            runners:[],
            runner:null,
            path:null,
            error:''
        }
    }

    getRunners=()=>{
        getRunnersService().then(res=>{
            this.setState({runners:res.data})
        })
    }

    getRunner=(runner_id)=>{
        this.setState({path:null})
        getRunnerService(runner_id).then(res=>{
            this.setState({runner:res.data})
        }).catch(e=>console.log(e))
    }

    getPath=(runner_id)=>{
        getRunnerPathService(runner_id).then(res=>{
            if(res.status===200){
            this.setState({path:res.data})
            this.setState({error:''})
            }else {
                this.setState({path:null})
                this.setState({error:'There is no path for this runner'})
            }
        }).catch(e=>console.log(e))
    }

    render() {
        return (
            <div className={'container'}>
                <div className={'row'}>
                    <div className={'col'}>
                        <div style={{textAlign:'center'}}>
                            <h3 style={{opacity:'0.6'}}>
                                List of runners
                            </h3>
                        </div>
                        <div style={{textAlign:'center'}}>
                            {this.state.runners.length===0 &&
                            <button className={"btn btn-primary"} 
                            onClick={this.getRunners}
                            >Get Runners</button>}
                            <div style={{height:'300px',overflow:'auto'}}>
                            {
                                this.state.runners.length!==0 &&
                                this.state.runners.map(runner=>{
                                    return <p key={runner.id} onClick={()=>this.getRunner(runner.id)}>
                                        {runner.id}
                                        </p>
                                })
                            }
                            </div>
                        </div>
                    </div>
                    <div className={'col'}>
                    <div style={{textAlign:'center'}}>
                            <h3 style={{opacity:'0.6'}}>
                                Runner Details:
                            </h3>
                            {
                                this.state.runner!==null && 
                                <div>
                                    <p>Name: {this.state.runner.name}</p>
                                    <p>Device:  {this.state.runner.device}</p>
                                    <p>Activity Level:  {this.state.runner.activity_level}</p>
                                    <button className={"btn btn-primary"} onClick={()=>this.getPath(this.state.runner.id)}>
                                        Get Path
                                    </button>
                                </div>
                            }
                        </div>
                    </div>
                    <div className={'col-6'}>
                    <div style={{textAlign:'center'}}>
                            <h3 style={{opacity:'0.6'}}>
                                Path Details:
                            </h3>
                            {   
                                this.state.path!==null && 
                                <div>
                                    <p>Average Heart Rate: {this.state.path.heart_rate_avg} [bpm]</p>
                                    <p>Average Speed:  {this.state.path.speed_avg} [m/s]</p>
                                    <table>
                                        <tr>
                                            <th>X-coordinate</th>
                                            <th>Y-coordinate</th>
                                            <th>Distance [km]</th>
                                            <th>Minute</th>
                                        </tr>
                                        {
                                            this.state.path.points.map((point,id)=>{
                                                return <tr key={point.distance}>
                                                    <td>{point.x_path}</td>
                                                    <td>{point.y_path}</td>
                                                    <td>{point.distance}</td>
                                                    <td>{id}</td>
                                                </tr>
                                            })
                                        }
                                        </table>
                                </div>
                            }
                            {
                                this.state.error.length>0 && <p>{this.state.error}</p>
                            }
                    </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Runners;