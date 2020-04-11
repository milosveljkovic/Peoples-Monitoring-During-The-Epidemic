import Dashboard from './pages/dashboard/dashboard'

var routes= [
    {
        path: "/dashboard",
        name: "Dashboard",
        component: Dashboard,
    },
    {
        path: "*",
        name: "Dashboard",
        component: Dashboard,
    }
]

export default routes;