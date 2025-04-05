<template>
  <nav class="main-menu">
    <div class="nav-item">
      <span class="nav-title">Tom</span>
      <div class="dropdown-content">
        <div class="dropdown-item">Tom</div>
        <div class="dropdown-item">Tom</div>
        <div class="dropdown-item">Tom</div>
      </div>
    </div>
    <div class="nav-item">
      <span class="nav-title">Tom</span>
      <div class="dropdown-content">
        <div class="dropdown-item">Tom</div>
        <div class="dropdown-item">Tom</div>
        <div class="dropdown-item">Tom</div>
      </div>
    </div>
    <div class="nav-item">
      <span class="nav-title">Tom</span>
      <div class="dropdown-content">
        <div class="dropdown-item">Tom</div>
        <div class="dropdown-item">Tom</div>
        <div class="dropdown-item">Tom</div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'MainMenu'
};
</script>

<style scoped>
.main-menu {
  background-color: #333;
  padding: 0;
  margin: 0;
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
  height: 50px;
  display: flex;
  padding-left: 20px;
}

.nav-item {
  position: relative;
  padding: 0 20px;
  color: white;
  cursor: pointer;
  font-family: Trebuchet MS, sans-serif;
  height: 100%;
  display: flex;
  align-items: center;
}

.nav-item:hover {
  background-color: #444;
}

.dropdown-content {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #444;
  min-width: 200px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  z-index: 1001;
}

.nav-item:hover .dropdown-content {
  display: block;
}

.dropdown-item {
  padding: 10px 20px;
  color: white;
  cursor: pointer;
  font-family: Trebuchet MS, sans-serif;
}

.dropdown-item:hover {
  background-color: #555;
}
</style> 