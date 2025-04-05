<template>
  <div class="format-selector">
    <label for="format">Format:</label>
    <select id="format" v-model="selectedFormat" class="format-select">
      <option value="dms">Grader, minuter, sekunder</option>
      <option value="decimal">Decimalgrader</option>
      <option value="nmea">GNG</option>
      <option value="line">Topsky Line</option>
    </select>
  </div>
</template>

<script>
export default {
  name: 'FormatSelector',
  props: {
    modelValue: {
      type: String,
      required: true
    }
  },
  computed: {
    selectedFormat: {
      get() {
        return this.modelValue;
      },
      set(value) {
        this.$emit('update:modelValue', value);
      }
    }
  }
};
</script>

<style scoped>
.format-selector {
  display: flex;
  align-items: center;
  gap: 9px;
}

.format-select {
  margin-bottom: 0;
  width: auto;
  padding: 4px 8px;
  font-size: 0.9em;
  height: 28px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

label {
  margin-bottom: 0;
  font-size: 0.9em;
  color: #333;
}
</style> 