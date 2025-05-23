/**
 * Selling Partner APIs for Fulfillment Outbound
 * The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
 *
 * The version of the OpenAPI document: 2020-07-01
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'

/**
 * The Weight model module.
 * @module fulfillmentoutbound_v2020_07_01/model/Weight
 * @version 2020-07-01
 */
export class Weight {
  /**
   * Constructs a new <code>Weight</code>.
   * The weight.
   * @alias module:fulfillmentoutbound_v2020_07_01/model/Weight
   * @class
   * @param unit {module:fulfillmentoutbound_v2020_07_01/model/Weight.UnitEnum} The unit of weight.
   * @param value {String} The weight value.
   */
  constructor (unit, value) {
    this.unit = unit
    this.value = value
  }

  /**
   * Constructs a <code>Weight</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:fulfillmentoutbound_v2020_07_01/model/Weight} obj Optional instance to populate.
   * @return {module:fulfillmentoutbound_v2020_07_01/model/Weight} The populated <code>Weight</code> instance.
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
      obj = obj || new Weight()
      if (data.hasOwnProperty('unit')) { obj.unit = ApiClient.convertToType(data.unit, 'String') }
      if (data.hasOwnProperty('value')) { obj.value = ApiClient.convertToType(data.value, 'String') }
    }
    return obj
  }
}

/**
 * Allowed values for the <code>unit</code> property.
 * @enum {String}
 * @readonly
 */
Weight.UnitEnum = {

  /**
     * value: "KG"
     * @const
     */
  KG: 'KG',

  /**
     * value: "KILOGRAMS"
     * @const
     */
  KILOGRAMS: 'KILOGRAMS',

  /**
     * value: "LB"
     * @const
     */
  LB: 'LB',

  /**
     * value: "POUNDS"
     * @const
     */
  POUNDS: 'POUNDS'
}

/**
 * The unit of weight.
 * @member {module:fulfillmentoutbound_v2020_07_01/model/Weight.UnitEnum} unit
 */
Weight.prototype.unit = undefined

/**
 * The weight value.
 * @member {String} value
 */
Weight.prototype.value = undefined
