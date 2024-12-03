import React, { useState, useEffect } from 'react';
import { fetchDocuments } from '../../services/api'; // Adjust path if needed
import './DocumentSearch.css';


function DocumentSearch() {
    const [documents, setDocuments] = useState([]);
    const [filters, setFilters] = useState({
        search: '',
        document_type: '',
        status: '',
        created_at: ''
    });

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetchDocuments(filters);
            setDocuments(response.data);
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
        <div className="document-search">
            <input 
                type="text" 
                name="search" 
                value={filters.search} 
                onChange={handleInputChange} 
                placeholder="Search by shipment ID"
                className="search-bar"
            />
            <select 
                name="document_type" 
                value={filters.document_type} 
                onChange={handleInputChange}
                className="dropdown"
            >
                <option value="">All Types</option>
                <option value="customs">Customs</option>
                <option value="internal">Internal</option>
                <option value="shipment">Shipment</option>
            </select>
            <select 
                name="status" 
                value={filters.status} 
                onChange={handleInputChange}
                className="dropdown"
            >
                <option value="">All Status</option>
                <option value="draft">Draft</option>
                <option value="pending">Pending</option>
                <option value="approved">Approved</option>
                <option value="rejected">Rejected</option>
            </select>
            <input 
                type="date" 
                name="created_at" 
                value={filters.created_at} 
                onChange={handleInputChange} 
                className="date-picker"
            />
            <div className="documents-list">
                {documents.map(doc => (
                    <div key={doc.id} className="document-item">
                        <h3>{doc.title}</h3>
                        <p>Status: {doc.status}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default DocumentSearch;
