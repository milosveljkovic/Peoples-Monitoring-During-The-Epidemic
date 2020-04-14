import Dashboard from './pages/dashboard/dashboard'
import Runners from './pages/runners/runners';

var routes= [
    {
        path: "/dashboard",
        name: "Dashboard",
        component: Dashboard,
    },
    {
        path: "/runners",
        name: "Runners",
        component: Runners,
    },
    {
        path: "*",
        name: "Dashboard",
        component: Dashboard,
    }
]

export default routes;