import React, { useState } from 'react';
import { uploadDocument } from '../../services/api';

function DocumentUpload() {
    const [file, setFile] = useState(null);
    const [documentType, setDocumentType] = useState("");
    const [status, setStatus] = useState("draft");

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        if (!file) {
            alert("Please select a file to upload");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);
        formData.append("document_type", documentType);
        formData.append("status", status);

        try {
            const response = await uploadDocument(formData);
            console.log("File uploaded successfully", response.data);
        } catch (error) {
            console.error("File upload failed", error);
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <select onChange={(e) => setDocumentType(e.target.value)}>
                <option value="customs">Customs Document</option>
                <option value="internal">Internal Document</option>
                <option value="shipment">Shipment Document</option>
            </select>
            <select onChange={(e) => setStatus(e.target.value)}>
                <option value="draft">Draft</option>
                <option value="pending">Pending Review</option>
                <option value="approved">Approved</option>
                <option value="rejected">Rejected</option>
            </select>
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
}

export default DocumentUpload;
