import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const coordinateService = {
  async convertCoordinates(coordinates, inputFormat) {
    try {
      console.log('Sending coordinates:', coordinates);
      console.log('Input format:', inputFormat);
      const response = await axios.post(`${API_URL}/convert`, {
        coordinates,
        input_format: inputFormat
      });
      console.log('Response:', response.data);
      return response.data;
    } catch (error) {
      console.error('Konverteringsfel:', error);
      throw error;
    }
  },

  parseCoordinates(input) {
    const parsed = input
      .split('\n')
      .map(line => line.trim())
      .filter(line => line.length > 0)
      .flatMap(line => {
        // Dela upp raden i koordinatpar
        const coords = line.split(/\s+/);
        return coords;
      });
    console.log('Parsed coordinates:', parsed);
    return parsed;
  }
}; 