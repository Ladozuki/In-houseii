import React, { useState, useEffect } from 'react';
import { fetchShipments } from '../../services/api';

function ShipmentList() {
    const [shipments, setShipments] = useState([]);
    const [filters, setFilters] = useState({
        customs_status: '',
        client_name: ''
    });

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetchShipments(filters);
            setShipments(response.data);
        };

        fetchData();
    }, [filters]);

    const handleInputChange = (e) => {
        setFilters({
            ...filters,
            [e.target.name]: e.target.value
        });
    };

    return (
        <div>
            <input 
                type="text" 
                name="client_name" 
                value={filters.client_name} 
                onChange={handleInputChange} 
                placeholder="Search by client name"
            />
            <select name="customs_status" value={filters.customs_status} onChange={handleInputChange}>
                <option value="">All Status</option>
                <option value="not_started">Not Started</option>
                <option value="in_progress">In Progress</option>
                <option value="completed">Completed</option>
            </select>
            <div>
                {shipments.map(shipment => (
                    <div key={shipment.id}>
                        <h3>{shipment.client_name}</h3>
                        <p>Status: {shipment.customs_status}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default ShipmentList;
