import axios from 'axios'
import Url from './Url.class.js'
export default class Http {
  beforeCallback = null
  successCallback = null
  failCallback = null
  defaultCallback = null
  static send (args) {
    let instance = new Http()

    if (instance.beforeCallback) instance.beforeCallback()

    axios({
      url: Url[args.url],
      method: args.method,
      baseURL: window.baseUrl,
      withCredentials: true,
    }).then(response => {
      instance.dispense(response.data)
      if (instance.defaultCallback) instance.defaultCallback()
    }).catch(error => {
      if (instance.defaultCallback) instance.defaultCallback()
    })
    return instance
  }
  dispense (response) {
    this.notice(response.description)
    switch (response.code) {
      case 200:
        if (this.successCallback) this.successCallback(response.data)
        break
      default:
        if (this.failCallback) this.failCallback(response)
    }
  }
  before (callback) {
    this.beforeCallback = callback
    return this
  }
  success (callback) {
    this.successCallback = callback
    return this
  }
  fail (callback) {
    this.failCallback = callback
    return this
  }
  default (callback) {
    this.defaultCallback = callback
    return this
  }
  notice (message) {
    if (!("Notification" in window)) {
      alert("This browser does not support desktop notification");
    }
    else if (Notification.permission === "granted") {
      new Notification('success', {
        dir: 'ltr',
        body: message
      })
    }
    else if (Notification.permission !== 'denied') {
      Notification.requestPermission((permission) => {
        if (permission === "granted") {
          new Notification('error', {
            dir: 'ltr',
            body: message
          })
        }
      });
    }

  }

}
