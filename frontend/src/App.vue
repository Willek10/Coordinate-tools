<template>
  <div class="app">
    <MainMenu />
    <div class="container">
      <div class="content">
        <div class="input-output-container">
          <CoordinateInput v-model="coordinates" />
          <CoordinateOutput 
            :results="results" 
            :input-format="inputFormat"
            @update:inputFormat="inputFormat = $event"
          />
        </div>
        <div class="controls">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MainMenu from './components/MainMenu.vue';
import CoordinateInput from './components/CoordinateInput.vue';
import CoordinateOutput from './components/CoordinateOutput.vue';
import FormatSelector from './components/FormatSelector.vue';
import { coordinateService } from './services/coordinateService';

export default {
  name: 'App',
  components: {
    MainMenu,
    CoordinateInput,
    CoordinateOutput,
    FormatSelector
  },
  data() {
    return {
      coordinates: '',
      results: [],
      inputFormat: 'dms'
    };
  },
  watch: {
    coordinates: {
      handler: 'convertCoordinates',
      immediate: true
    },
    inputFormat: {
      handler: 'convertCoordinates',
      immediate: true
    }
  },
  methods: {
    async convertCoordinates() {
      if (!this.coordinates.trim()) {
        this.results = [];
        return;
      }
      try {
        const coords = coordinateService.parseCoordinates(this.coordinates);
        this.results = await coordinateService.convertCoordinates(coords, this.inputFormat);
      } catch (error) {
        console.error('Konverteringsfel:', error);
        this.results = [];
      }
    }
  }
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Trebuchet MS, sans-serif;
  background-color: #f5f6fa;
  color: #2c3e50;
  line-height: 1.6;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.container {
  flex: 1;
  padding: 0 1rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
  padding-top: 60px;
}

.content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.input-output-container {
  display: flex;
  gap: 20px;
  height: calc(100vh - 200px);
}

.controls {
  display: flex;
  gap: 1rem;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}
</style> 