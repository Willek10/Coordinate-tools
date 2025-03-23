<template>
  <div class="container">
    <h1>Koordinatkonverterare</h1>
    <div class="input-section">
      <div class="input-group">
        <label for="latitude">Latitud:</label>
        <input type="number" id="latitude" v-model="latitude" step="any" placeholder="Ex: 59.3293">
      </div>
      <div class="input-group">
        <label for="longitude">Longitud:</label>
        <input type="number" id="longitude" v-model="longitude" step="any" placeholder="Ex: 18.0686">
      </div>
      <div class="input-group">
        <label for="format">Format:</label>
        <select id="format" v-model="inputFormat">
          <option value="decimal">Decimalgrader</option>
          <option value="dms">Grader, minuter, sekunder</option>
        </select>
      </div>
      <button @click="convertCoordinates" :disabled="!isValid">Konvertera</button>
    </div>
    
    <div class="output-section" v-if="result">
      <h2>Resultat:</h2>
      <div class="result">
        <p v-if="inputFormat === 'decimal'">
          DMS: {{ formatDMSResult(result) }}
        </p>
        <p v-else>
          Decimalgrader: {{ formatDecimalResult(result) }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      latitude: '',
      longitude: '',
      inputFormat: 'decimal',
      result: null
    }
  },
  computed: {
    isValid() {
      return this.latitude !== '' && this.longitude !== '';
    }
  },
  methods: {
    async convertCoordinates() {
      try {
        const response = await axios.post('http://localhost:8000/convert', {
          latitude: parseFloat(this.latitude),
          longitude: parseFloat(this.longitude),
          input_format: this.inputFormat
        });
        this.result = response.data;
      } catch (error) {
        alert('Ett fel uppstod vid konvertering: ' + error.message);
      }
    },
    formatDMSResult(result) {
      return `${result.latitude.degrees}° ${result.latitude.minutes}' ${result.latitude.seconds}" N, ` +
             `${result.longitude.degrees}° ${result.longitude.minutes}' ${result.longitude.seconds}" E`;
    },
    formatDecimalResult(result) {
      return `${result.latitude}, ${result.longitude}`;
    }
  }
}
</script>

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.input-section {
  margin: 20px 0;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
}

.input-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.output-section {
  margin-top: 20px;
  padding: 20px;
  background-color: #e8f5e9;
  border-radius: 8px;
}

.result {
  font-family: monospace;
  font-size: 1.1em;
}
</style> 