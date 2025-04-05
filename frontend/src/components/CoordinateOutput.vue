<template>
  <div class="output-section">
    <div class="output-header">
      <h2>Utdata</h2>
      <FormatSelector :modelValue="inputFormat" @update:modelValue="$emit('update:inputFormat', $event)" />
    </div>
    <div class="output-wrapper">
      <textarea
        :value="formattedOutput"
        readonly
        class="output-textarea"
        placeholder="Konverterade koordinater visas här..."
      ></textarea>
    </div>
  </div>
</template>

<script>
import FormatSelector from './FormatSelector.vue';

export default {
  name: 'CoordinateOutput',
  components: {
    FormatSelector
  },
  props: {
    results: {
      type: Array,
      required: true
    },
    inputFormat: {
      type: String,
      required: true
    }
  },
  computed: {
    formattedOutput() {
      if (!this.results.length) return '';
      return this.results.map(result => {
        if (this.inputFormat === 'dms') {
          return this.formatDMSResult(result);
        } else if (this.inputFormat === 'nmea') {
          return this.formatNMEAResult(result);
        } else if (this.inputFormat === 'line') {
          return this.formatLINEResult(result);
        } else {
          return this.formatDecimalResult(result);
        }
      }).join('\n');
    }
  },
  methods: {
    formatDMSResult(result) {
      if (typeof result.latitude === 'object') {
        const lat = result.latitude;
        const lon = result.longitude;
        return `${lat.degrees}°${lat.minutes}'${lat.seconds}"N, ${lon.degrees}°${lon.minutes}'${lon.seconds}"E`;
      }
      const lat = this.decimalToDMS(result.latitude);
      const lon = this.decimalToDMS(result.longitude);
      return `${lat} ${lon}`;
    },
    formatDecimalResult(result) {
      if (typeof result.latitude === 'object') {
        const lat = result.latitude;
        const lon = result.longitude;
        const latDecimal = lat.degrees + lat.minutes/60 + lat.seconds/3600;
        const lonDecimal = lon.degrees + lon.minutes/60 + lon.seconds/3600;
        return `${latDecimal.toFixed(6)} ${lonDecimal.toFixed(6)}`;
      }
      return `${result.latitude.toFixed(6)}, ${result.longitude.toFixed(6)}`;
    },
    formatNMEAResult(result) {
      const lat = this.decimalToNMEA(result.latitude, 'lat');
      const lon = this.decimalToNMEA(result.longitude, 'lon');
      return `${lat}, ${lon}`;
    },
    formatLINEResult(result) {
      const lat = this.decimalToNMEA(result.latitude, 'lat');
      const lon = this.decimalToNMEA(result.longitude, 'lon');
      return `${lat}, ${lon}`;
    },
    decimalToDMS(decimal) {
      const degrees = Math.floor(Math.abs(decimal));  // Hämta grader
      const minutesDecimal = (Math.abs(decimal) - degrees) * 60;  // Beräkna minuter i decimalform
      const minutes = Math.floor(minutesDecimal);  // Hämta hela minuter
      const secondsDecimal = (minutesDecimal - minutes) * 60;  // Beräkna sekunder med decimaler
      const seconds = Math.floor(secondsDecimal);  // Hämta hela sekunder
      const milliseconds = Math.round((secondsDecimal - seconds) * 1000);  // Beräkna millisekunder

      const direction = decimal >= 0 ? 'N' : 'S';  // Bestäm riktning (N/S)

      // Formatera DMS: Grader, minuter, sekunder, millisekunder
      return `${direction}${degrees.toString().padStart(3, '0')}.${minutes.toString().padStart(2, '0')}.${seconds.toString().padStart(2, '0')}.${milliseconds.toString().padStart(3, '0')}`;
    },

    // return `${direction}${degrees.toString().padStart(3, '0')}.${minutes.toString().padStart(2, '0')}.${Math.floor(secondsDecimal).toString().padStart(2, '0')}.${milliseconds.toString().padStart(3, '0')}`;
    decimalToNMEA(decimal, type) {
      const degrees = Math.floor(Math.abs(decimal));
      const minutes = (Math.abs(decimal) - degrees) * 60;

      // Om det är latitud, använd N/S, annars använd E/W
      const direction = type === 'lat'
        ? (decimal >= 0 ? 'N' : 'S')  // Latitud
        : (decimal >= 0 ? 'E' : 'W'); // Longitud

      return `${direction}${degrees.toString().padStart(3, '0')}.${minutes.toFixed(2).padStart(5, '0')}`;
    }
  }
};
</script>

<style scoped>
.output-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 20px;
  border-radius: 3px;
  max-width: 600px;
}

.output-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

h2 {
  margin: 0;
  color: #333;
  font-size: 1.1em;
}

.output-wrapper {
  flex: 1;
  position: relative;
}

.output-textarea {
  width: 99%;
  height: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  resize: none;
  font-family: Trebuchet MS, sans-serif;
  font-size: 0.9em;
  line-height: 1.4;
  background-color: #f8f8f8;
  pointer-events: none;
  overflow-y: auto;
}

.output-textarea::-webkit-scrollbar {
  width: 8px;
  display: none;
}

.output-wrapper:hover .output-textarea::-webkit-scrollbar {
  display: block;
}

.output-textarea::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.output-textarea::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

.output-textarea::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>
