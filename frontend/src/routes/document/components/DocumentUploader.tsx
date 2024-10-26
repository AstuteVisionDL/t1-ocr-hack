
import React, { useState } from 'react';
import { uploadDocument, DocumentResponse } from '../services/documentService';

const DocumentUploader: React.FC = () => {
    const [file, setFile] = useState<File | null>(null);
    const [response, setResponse] = useState<DocumentResponse[] | null>(null);
    const [error, setError] = useState<string | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setFile(event.target.files[0]);
        }
    };

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setError(null); // Reset error state

        if (!file) {
            setError('Please select a file.');
            return;
        }

        try {
            const data = await uploadDocument(file);
            setResponse(data); // Set response data
        } catch (error) {
            setError('Failed to upload document.' + error); // Handle error
        }
    };

    return (
        <div>
            <h1>Upload Document</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} />
                <button type="submit">Upload</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {response && (
                <div>
                    <h2>Response:</h2>
                    <pre>{JSON.stringify(response, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default DocumentUploader;
