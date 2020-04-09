import Device from './pages/device'
import Dashboard from './pages/dashboard'

var routes= [
    {
        path: "/device",
        name: "Device",
        component: Device,
    },
    {
        path: "/dashboard",
        name: "Dashboard",
        component: Dashboard,
    },
    {
        path: "*",
        name: "Device",
        component: Device,
    }
]

export default routes;