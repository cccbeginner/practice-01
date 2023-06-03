<template>
  <div>
    <h2>Update Profile</h2>
    <p>Username: {{ username }}</p>
    <input type="date" v-model="newBirthday" /><br />
    <input type="password" v-model="newPassword" placeholder="New Password" /><br />
    <input type="password" v-model="confirmNewPassword" placeholder="Confirm Password" /><br />
    <p v-if="newPassword !== confirmNewPassword">Passwords do not match</p>
    <button @click="updateProfile">Update</button>
    <router-link to="/">Profile</router-link>
  </div>
</template>

<script>
import axios from '../axios';
import api from '../api';

export default {

  data() {
    return {
      username: '',
      newPassword: '',
      confirmNewPassword: '',
      newBirthday: '',
    };
  },
  // Other component code here

  mounted() {
    this.fetchUserData();
  },
  methods: {
    fetchUserData() {
      // Perform the AJAX request
      axios.get(api.USER_URL)
        .then(response => {
          // Set the data received from the response to the component's data
          this.username = response.data.username;
          this.newBirthday = response.data.birthday;
          // Other data handling or logic here
        })
        .catch(error => {
          // Handle the error
          if(error.response){
            const detail = error.response.data.detail
            alert(error.message+'\n'+detail);
            if (detail.includes("JWTError")){
              localStorage.removeItem('token');
              this.$router.go(0);
            }
          }else alert(error);
        });
    },
    updateProfile() {
      // Your form submission logic here
      if(this.newPassword !== this.confirmNewPassword){
        alert("Passwords do not match");
        return;
      }
      axios.put(api.USER_URL, {
        username: this.username,
        password: (this.newPassword !== '') ? this.newPassword : null,
        birthday: this.newBirthday,
      })
        .then(() => {
          // On success, redirect to profile page
          this.$router.push('/');
        })
        .catch(error => {
          // Handle error
          if(error.response){
            const detail = error.response.data.detail
            alert(error.message+'\n'+detail);
            if (detail.includes("JWTError")){
              localStorage.removeItem('token');
              this.$router.go(0);
            }
          }else alert(error);
        });
    }
  }
};
</script>
