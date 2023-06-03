<template>
  <div>
    <h2>Register</h2>
    <input type="text" v-model="username" placeholder="Username" /><br />
    <input type="date" v-model="birthday" /><br />
    <input type="password" v-model="password" placeholder="Password" /><br />
    <input type="password" v-model="confirmPassword" placeholder="Confirm Password" /><br />
    <p v-if="password !== confirmPassword">Passwords do not match</p>
    <button @click="register">Submit</button>
    <router-link to="/login">Login</router-link>
  </div>
</template>

<script>
import axios from 'axios';
import api from '../api';

export default {
  data() {
    return {
      username: '',
      birthday: '',
      password: '',
      confirmPassword: '',
    };
  },
  methods: {
    register() {
      // Handle registration logic
      if(this.username === ''){
        alert("Username cannot be empty.")
        return;
      }
      if(this.password === ''){
        alert("Password cannot be empty.")
        return;
      }
      if(this.password !== this.confirmPassword){
        alert("Passwords do not match!")
        return;
      }
      if(this.birthday === ''){
        alert("Birthday cannot be empty.")
        return;
      }
      axios.post(api.USER_URL, {
          username : this.username,
          birthday : this.birthday,
          password : this.password,
        })
          .then(() => {
            this.$router.push('/');
          })
          .catch(error => {
            // Handle the error
            if(error.response){
              const detail = error.response.data.detail
              alert(error.message+'\n'+detail);
            }else alert(error);
          });
    },
  },
};
</script>
