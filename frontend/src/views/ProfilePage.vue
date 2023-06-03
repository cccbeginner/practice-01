<template>
  <div>
    <h2>User Profile</h2>
    <p>Username: {{ username }}</p>
    <p>Birthday: {{ birthday }}</p>
    <p>Create Time: {{ createTime }}</p>
    <p>Last Login Time: {{ lastLoginTime }}</p>
    <button @click="deleteUser">Delete User</button>
    <button @click="logout">Logout</button>
    <router-link to="/update">Update</router-link>
  </div>
</template>

<script>
import axios from '../axios';
import api from '../api';

export default {
  data() {
    return {
      username: '',
      birthday: '',
      createTime: '',
      lastLoginTime: '',
    };
  },
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
          this.birthday = response.data.birthday;
          this.createTime = response.data.create_time;
          this.lastLoginTime = response.data.last_login;

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
    deleteUser() {
      // Show confirmation popup
      if (confirm('Are you sure you want to delete your account?')) {
        // Handle account deletion logic

        axios.delete(api.USER_URL, {
          data:{
            username : this.username,
            password : null,
            birthday : null,
          }
        })
          .then(() => {
            // Set the data received from the response to the component's data
            localStorage.removeItem('token');
            this.$router.go(0);
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
      }
    },
    logout() {
      // Handle logout logic
      if (confirm('Logout?')) {
        // Handle account deletion logic
        localStorage.removeItem('token');
        this.$router.go(0);
      }
    },
  },
};
</script>
