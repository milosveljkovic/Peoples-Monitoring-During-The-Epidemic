import React, { Component } from 'react';
import { testRequest } from '../services.js/runner.service'
import './runnerform.css'

class RunnerForm extends Component {

    constructor(props) {
        super(props);

        this.state = {
            email: '',
            name: '',
            device: '',
            activity_level: 'Sedentary',
            x: 0, y: 0,
            goal_distance: 1,
            success_response: '',
            show_response: false,
            path_name:''
        }
    }

    onChange = (event) => {
        this.setState({ [event.target.name]: event.target.value })
    }

    onSubmit = () => {
        const runner = {
            id: this.state.email,
            name: this.state.name,
            device: this.state.device,
            activity_level: this.state.activity_level,
            x: this.state.x,
            y: this.state.y,
            goal_distance: this.state.goal_distance,
            path_name:this.state.path_name
        }
        testRequest(runner)
            .then(response => {
                // this.setState({ success_response: response.data.message, show_response: true })
            })

        this.props.setDistance(this.state.goal_distance);
    }

    render() {
        const { email, name, device, x, y, goal_distance,path_name } = this.state;
        return <div style={{ textAlign: 'center' }}>
            <p style={{ margin: "0px" }}>Runners form</p>
            {
                this.state.show_response ?
                    <small style={{ opacity: "0.7", color: "green" }}>Success!</small>
                    :
                    <small style={{ opacity: "0.2" }}>(message)</small>
            }
            <form>
                <div className="form row mt-3">
                    <label htmlFor="exampleInputEmail1">Email address:</label>
                    <input
                        onChange={this.onChange}
                        name={'email'}
                        value={email}
                        type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
                </div>
                <div className="row">
                    <div className="col">
                    <label htmlFor="exampleInputPassword1">Name:</label>
                    <input
                        onChange={this.onChange}
                        name={'name'}
                        value={name}
                        type="text" className="form-control" id="name" />
                    </div>
                    <div className="col">
                    <label htmlFor="exampleInputPassword1">Device:</label>
                    <input
                        onChange={this.onChange}
                        name={'device'}
                        value={device}
                        type="text" className="form-control" id="device" />
                </div>
                </div>
                <div className="form row mt-3">
                    <label htmlFor="path_name">Path name:</label>
                    <input
                        onChange={this.onChange}
                        name={'path_name'}
                        value={path_name}
                        type="path_name" className="form-control" id="path_name"/>
                </div>
                <div className="row">
                    <div className="col">
                        <label htmlFor="exampleInputPassword1">x-coordinate:</label>
                        <input
                            onChange={this.onChange}
                            name={'x'}
                            value={x} min='0' max='1000'
                            type="number" className="form-control" id="x" />
                    </div>
                    <div className="col">
                        <label htmlFor="exampleInputPassword1">y-coordinate:</label>
                        <input
                            onChange={this.onChange}
                            name={'y'}
                            value={y} min='0' max='1000'
                            type="number" className="form-control" id="y" />
                    </div>
                    <div className="col">
                        <label htmlFor="exampleInputPassword1">Distance(km):</label>
                        <input
                            onChange={this.onChange}
                            name={'goal_distance'}
                            value={goal_distance} min='1' max='100'
                            type="number" className="form-control" id="goal_distance" />
                    </div>
                </div>
                <div className="form row mt-3">
                    <label className="mx-3">Select activity level</label>
                    <select name="activity_level" className="form-control mx-3" onChange={this.onChange}>
                        <option value={'Sedentary'} key={'Sedentary'}>Sedentary</option>
                        <option value={'Somewhat active'} key={'Somewhat active'}>Somewhat active</option>
                        <option value={'Active'} key={'Active'}>Active</option>
                        <option value={'Very active'} key={'Very active'}>Very active</option>
                    </select>
                </div>
            </form>
            <button style={{ margin: '10px' }} className="btn btn-primary" onClick={this.onSubmit}>Submit</button>
        </div>
    }
}

export default RunnerForm;