/**
 * The Selling Partner API for Amazon Seller Wallet Open Banking API
 * The Selling Partner API for Seller Wallet (Seller Wallet API) provides financial information that is relevant to a seller's Seller Wallet account. You can obtain financial events, balances, and transfer schedules for Seller Wallet accounts. You can also schedule and initiate transactions.
 *
 * The version of the OpenAPI document: 2024-03-01
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'

/**
 * The DeleteTransferSchedule model module.
 * @module sellerWallet_2024_03_01/model/DeleteTransferSchedule
 * @version 2024-03-01
 */
export class DeleteTransferSchedule {
  /**
   * Constructs a new <code>DeleteTransferSchedule</code>.
   * The response returned when the schedule transfer&#39;s delete request is successful.
   * @alias module:sellerWallet_2024_03_01/model/DeleteTransferSchedule
   * @class
   * @param code {String} A success code that specifies that the delete operation was successful. For example, HTTP 200.
   * @param message {String} A message that describes the success condition of the delete schedule transaction.
   */
  constructor (code, message) {
    this.code = code
    this.message = message
  }

  /**
   * Constructs a <code>DeleteTransferSchedule</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:sellerWallet_2024_03_01/model/DeleteTransferSchedule} obj Optional instance to populate.
   * @return {module:sellerWallet_2024_03_01/model/DeleteTransferSchedule} The populated <code>DeleteTransferSchedule</code> instance.
   */
  static constructFromObject (data, obj) {
    if (data) {
      switch (typeof data) {
        case 'string':
          obj = String(data)
          break
        case 'number':
          obj = Number(data)
          break
        case 'boolean':
          obj = Boolean(data)
          break
      }
      obj = obj || new DeleteTransferSchedule()
      if (data.hasOwnProperty('code')) { obj.code = ApiClient.convertToType(data.code, 'String') }
      if (data.hasOwnProperty('message')) { obj.message = ApiClient.convertToType(data.message, 'String') }
      if (data.hasOwnProperty('details')) { obj.details = ApiClient.convertToType(data.details, 'String') }
    }
    return obj
  }
}

/**
 * A success code that specifies that the delete operation was successful. For example, HTTP 200.
 * @member {String} code
 */
DeleteTransferSchedule.prototype.code = undefined

/**
 * A message that describes the success condition of the delete schedule transaction.
 * @member {String} message
 */
DeleteTransferSchedule.prototype.message = undefined

/**
 * Additional details that can help the caller understand the operation execution.
 * @member {String} details
 */
DeleteTransferSchedule.prototype.details = undefined
