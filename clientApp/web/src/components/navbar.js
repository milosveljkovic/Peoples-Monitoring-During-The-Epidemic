import React from 'react';
import {Link} from 'react-router-dom'
import './navbar.css'

class Navbar extends React.Component {

    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-light " style={{backgroundColor: "#e3f2fd"}}>
                <a className="navbar-brand">Monitoring App</a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText"
                        aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarText">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item">
                            <Link to="/dashboard" className={'nav-link'}>
                                Dashboard
                            </Link>
                        </li>
                    </ul>
                </div>
            </nav>
        )
    }

}

export default Navbar;