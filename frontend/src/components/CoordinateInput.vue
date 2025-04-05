<template>
  <div class="input-section">
    <div class="input-header">
      <h2>Indata</h2>
    </div>
    <div class="input-wrapper">
      <textarea
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        placeholder="Klistra in koordinater här..."
      ></textarea>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CoordinateInput',
  props: {
    modelValue: {
      type: String,
      required: true
    }
  },
  computed: {
    inputValue: {
      get() {
        return this.modelValue;
      },
      set(value) {
        this.$emit('update:modelValue', value);
      }
    }
  }
}
</script>

<style scoped>
.input-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 20px;
  border-radius: 3px;
  max-width: 600px;
}

.input-header {
  margin-bottom: 10px;
}

h2 {
  margin: 0;
  color: #333;
  font-size: 1.1em;
}

.input-wrapper {
  flex: 1;
  position: relative;
}

textarea {
  width: 99%;
  height: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  resize: none;
  font-family: Trebuchet MS, sans-serif;
  font-size: 0.9em;
  line-height: 1.4;
  overflow-y: auto;
}

textarea:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
}

/* Scrollbar styling */
textarea::-webkit-scrollbar {
  width: 8px;
  display: none;
}

.input-wrapper:hover textarea::-webkit-scrollbar {
  display: block;
}

textarea::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

textarea::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

textarea::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style> 