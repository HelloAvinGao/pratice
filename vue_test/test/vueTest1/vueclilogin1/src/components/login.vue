<template>
  <div v-bind:style="{ paddingTop: styles.AllmarginTops }">
    <div>
      <router-link to="/HelloWorld">点击进入HelloWorld</router-link>
      <br />
      <h2
        v-bind:style="{
          fontSize: styles.h2FontSize + 'px',
          color: styles.h2Color,
        }"
      >
        {{ $t("navbar.welcomeMsg") }}
      </h2>
    </div>
    <div id="loginForm">
      <a-form
        id="components-form-demo-normal-login"
        :form="form"
        class="login-form"
        @submit="handleSubmit"
      >
        <a-form-item>
          <a-input
            v-decorator="[
              'userName',
              {
                rules: [
                  { required: true, message: `${$t('navbar.usernameMsg')}` },
                ],
              },
            ]"
            :placeholder="$t('navbar.username')"
          >
            <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)" />
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-input
            v-decorator="[
              'password',
              {
                rules: [
                  { required: true, message: `${$t('navbar.passwordMSG')}` },
                ],
              },
            ]"
            type="password"
            :placeholder="$t('navbar.placeholderMsg')"
          >
            <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)" />
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-checkbox
            class="login-form-rememberpwd"
            v-decorator="[
              'remember',
              {
                valuePropName: 'checked',
                initialValue: true,
              },
            ]"
          >
            {{ $t("navbar.Remember") }}
          </a-checkbox>
          <a class="login-form-forgot" href="">
            {{ $t("navbar.forgotPWD") }}
          </a>
          <a-button type="primary" html-type="submit" class="login-form-button">
            {{ $t("navbar.login") }}
          </a-button>
        </a-form-item>
        <a-form-item>
          <p id="registerstyle">
            <router-link to="/register">
              {{ $t("navbar.register") }}
            </router-link>
          </p>
          <p class="login-form-langs" @click="changeLang()">
            {{ $t("language.name") }}
          </p>
        </a-form-item>
      </a-form>
    </div>
  </div>
</template>
<script>
export default {
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "normal_login" });
  },
  name: "Content",
  data() {
    return {
      styles: {
        h2FontSize: "35",
        h2Color: "#6da63d",
        AllmarginTops: "10vh",
      },
    };
  },
  methods: {
    changeLang: function() {
      let locale = localStorage.getItem("language") || "zh";
      let temp = locale === "zh" ? "en" : "zh";
      this.$i18n.locale = temp; //改变当前语言
      localStorage.language = temp;
      location.reload();
    },
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
          this.axios({
            url: "http://127.0.0.1:5000/login",
            method: "POST",
            crossdomain: true,
            params: values,
          }).then((res) => {
            this.token = res.data.token;
            if (this.token) {
              this.$store.commit("set_token", this.token); //调用store中的获取token方法，并将token存在store中
              this.$router.push("/HelloWorld");
            } else {
              this.$router.replace("/login");
            }
          });
        }
      });
    },
  },
};
</script>
<style>
#components-form-demo-normal-login .login-form {
  max-width: 300px;
}
#components-form-demo-normal-login .login-form-forgot,
.login-form-langs {
  float: right;
}
#components-form-demo-normal-login .login-form-button {
  width: 100%;
}
#loginForm {
  max-width: 20rem;
  margin: auto;
}
#registerstyle,
.login-form-rememberpwd {
  float: left;
}
</style>
