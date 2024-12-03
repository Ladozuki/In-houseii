import React, { useState, useEffect } from 'react';
import { fetchDashboardData } from '../../services/api';
import { PieChart, Pie, Tooltip } from 'recharts';

function Dashboard() {
    const [data, setData] = useState({});

    useEffect(() => {
        async function fetchData() {
            const response = await fetchDashboardData();
            setData(response);
        }
        fetchData();
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            <PieChart width={400} height={400}>
                <Pie
                    data={data.documents_by_status}
                    dataKey="count"
                    nameKey="status"
                    cx="50%"
                    cy="50%"
                    outerRadius={80}
                    fill="#8884d8"
                />
                <Tooltip />
            </PieChart>
        </div>
    );
}

export default Dashboard;
