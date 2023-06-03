<template>
  <div>
    <h2>Login</h2>
    <input type="text" v-model="username" placeholder="Username" /><br />
    <input type="password" v-model="password" placeholder="Password" /><br />
    <button @click="login">Submit</button>
    <router-link to="/register">Register</router-link>
  </div>
</template>

<script>
import axios from 'axios';
import api from '../api';

export default {
  // Your component's code

  methods: {
    login() {
      // Perform the POST request to the login endpoint
      axios.post(api.TOKEN_URL, {
        // Pass your login form data here
        grant_type: "password",
        username: this.username,
        password: this.password,
      },{
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      })
        .then(response => {
          // Store the JWT token in the frontend
          const token = response.data.access_token;
          localStorage.setItem('token', token);

          // Redirect to the desired page (e.g., profile page)
          this.$router.go(0);
        })
        .catch(error => {
          // Handle login error
          if(error.response){
            const detail = error.response.data.detail
            alert(error.message+'\n'+detail);
          }else alert(error);
        });
    }
  }
}
</script>