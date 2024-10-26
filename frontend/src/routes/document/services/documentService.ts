
import axios from 'axios';

// Define types for the response
export interface DocumentResponse {
    coordinates: number[][];
    content: string;
    language: string;
    signature: boolean;
}

const API_URL = 'http://127.0.0.1:8000/upload-document/'; // Change this to your FastAPI server URL

export const uploadDocument = async (file: File): Promise<DocumentResponse[]> => {
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await axios.post<DocumentResponse[]>(API_URL, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data; // Return the response data
    } catch (error) {
        console.error('Error uploading document:', error);
        throw error; // Throw error for handling in the component
    }
};
