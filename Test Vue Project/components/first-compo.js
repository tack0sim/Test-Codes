app.component("first-component", {
  data() {
    return {
      profiles: [],
    };
  },
  template:
    /* html*/
    `<div>
        <p>This is the first component</p>
        <second-component @submitted="profile" :profiles="profiles"></second-component>
    </div>`,

  methods: {
    profile(profile) {
      this.profiles.push(profile);
      console.log(profile);
    },
  },
});
