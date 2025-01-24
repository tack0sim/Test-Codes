app.component("second-component", {
  props: {
    profiles: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      count: 0,
      name: "",
    };
  },
  template:
    /*html */
    `<div>
      <p>Count is: {{ count }}</p>
      <p @click="increment">Click on me to increment the count!</p>

      <label for="name">Give your name:</label>
      <input id="name" v-model="name">
      <button @click="onSubmit">Submit</button>

      <div>
        <ul>
            <li v-for="profile in profiles">
            Name is: {{ profile }}<br/>
            </li>
        </ul>
      </div>
    </div>`,

  methods: {
    increment() {
      this.count++;
    },

    onSubmit() {
      let data = this.name;
      this.$emit("submitted", data);
    },
  },
});
