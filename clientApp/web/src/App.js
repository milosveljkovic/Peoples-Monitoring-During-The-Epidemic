import React from 'react';
import './App.css';
import {Switch, Route, Router} from 'react-router-dom';
import routes from './routes'
import Navbar from './components/navbar'
import { createBrowserHistory } from 'history';
import Dashboard from "./pages/dashboard/dashboard";
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
                    <div>
                        <div>
                            <Switch>
                                <Route exact path="/" component={Dashboard}/>
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