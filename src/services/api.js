import axios from 'axios';

const API = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/',
});

export default API;


export const uploadDocument = (formData) => {
    return API.post('/documents/upload', formData);
};

export const fetchDocuments = (filters) => {
    const queryParams = new URLSearchParams(filters).toString();
    return API.get(`/documents?${queryParams}`);
};

export const fetchShipments = (filters) => {
    const queryParams = new URLSearchParams(filters).toString();
    return API.get(`/shipments?${queryParams}`);
};

export const fetchDashboardData = () => {
    return API.get('dashboard/').then(res => res.data);
};