import React from 'react';
import './App.css';
import {Switch, Route, Router} from 'react-router-dom';
import routes from './routes'
import Device from "./pages/device";
import Navbar from './components/navbar'
import { createBrowserHistory } from 'history';
const history=createBrowserHistory();

class App extends React.Component {

    getRoutes = (routes) => {

        return routes.map((prop, key) => {
            return (
                <Route path={prop.path}
                       component={prop.component}
                       key={key}
                />
            );
        });
    }


    render() {

        return (
            <div>
                <Router history={history}>
                    <Navbar/>
                    <div className='content-div'>
                        <div id="wrapper" style={{'marginLeft': '64px', 'display': 'flex'}}>
                            <Switch>
                                <Route exact path="/" component={Device}/>
                                {
                                    this.getRoutes(routes)
                                }
                            </Switch>
                        </div>
                    </div>
                </Router>
            </div>
        );
    }
}

export default App;