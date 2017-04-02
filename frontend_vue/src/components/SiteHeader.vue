<template>
  <header id="site-header">
    <div class="uk-navbar-container">
      <div class="uk-container uk-container-expand">
        <nav class="uk-navbar-nav" uk-navbar>
          <div class="uk-navbar-left">
            <a class="uk-navbar-item uk-logo" href="/">Visualist</a>
            <ul class="uk-navbar-nav">
              <li>
                <a>Pages</a>
                <div class="uk-navbar-dropdown uk-navbar-dropdown-width-2">
                  <div class="uk-navbar-dropdown-grid uk-child-width-1-2" uk-grid>
                    <div>
                      <ul class="uk-nav uk-navbar-dropdown-nav">
                        <li><a href="/">Home</a></li>
                        <li><a href="/events">Events</a></li>
                        <li><a href="/orgs">Organizations</a></li>
                      </ul>
                    </div>
                    <div>
                      <ul class="uk-nav uk-navbar-dropdown-nav">
                        <li><a href="/search">Search</a></li>
                        <li><a href="#">About</a></li>
                      </ul>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
          <div class="uk-navbar-right">
            <div class="uk-navbar-item">
              <form action="javascript:void(0)">
                <input class="uk-input uk-form-width-small" type="text" placeholder="Search">
                <button class="uk-button uk-button-default"><span uk-icon="icon: search"></span></button>
              </form>
            </div>
          </div>
        </nav>
      </div>
    </div>
  </header>
</template>


<script>
export default {
  name: 'site-header',
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
</style>
