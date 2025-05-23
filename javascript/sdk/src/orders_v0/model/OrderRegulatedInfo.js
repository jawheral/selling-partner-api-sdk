/**
 * Selling Partner API for Orders
 * Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.   _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).
 *
 * The version of the OpenAPI document: v0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'
import { RegulatedInformation } from './RegulatedInformation.js'
import { RegulatedOrderVerificationStatus } from './RegulatedOrderVerificationStatus.js'

/**
 * The OrderRegulatedInfo model module.
 * @module orders_v0/model/OrderRegulatedInfo
 * @version v0
 */
export class OrderRegulatedInfo {
  /**
   * Constructs a new <code>OrderRegulatedInfo</code>.
   * The order&#39;s regulated information along with its verification status.
   * @alias module:orders_v0/model/OrderRegulatedInfo
   * @class
   * @param amazonOrderId {String} An Amazon-defined order identifier, in 3-7-7 format.
   * @param regulatedInformation {module:orders_v0/model/RegulatedInformation}
   * @param requiresDosageLabel {Boolean} When true, the order requires attaching a dosage information label when shipped.
   * @param regulatedOrderVerificationStatus {module:orders_v0/model/RegulatedOrderVerificationStatus}
   */
  constructor (amazonOrderId, regulatedInformation, requiresDosageLabel, regulatedOrderVerificationStatus) {
    this.amazonOrderId = amazonOrderId
    this.regulatedInformation = regulatedInformation
    this.requiresDosageLabel = requiresDosageLabel
    this.regulatedOrderVerificationStatus = regulatedOrderVerificationStatus
  }

  /**
   * Constructs a <code>OrderRegulatedInfo</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:orders_v0/model/OrderRegulatedInfo} obj Optional instance to populate.
   * @return {module:orders_v0/model/OrderRegulatedInfo} The populated <code>OrderRegulatedInfo</code> instance.
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
      obj = obj || new OrderRegulatedInfo()
      if (data.hasOwnProperty('AmazonOrderId')) { obj.amazonOrderId = ApiClient.convertToType(data.AmazonOrderId, 'String') }
      if (data.hasOwnProperty('RegulatedInformation')) { obj.regulatedInformation = RegulatedInformation.constructFromObject(data.RegulatedInformation) }
      if (data.hasOwnProperty('RequiresDosageLabel')) { obj.requiresDosageLabel = ApiClient.convertToType(data.RequiresDosageLabel, 'Boolean') }
      if (data.hasOwnProperty('RegulatedOrderVerificationStatus')) { obj.regulatedOrderVerificationStatus = RegulatedOrderVerificationStatus.constructFromObject(data.RegulatedOrderVerificationStatus) }
    }
    return obj
  }
}

/**
 * An Amazon-defined order identifier, in 3-7-7 format.
 * @member {String} amazonOrderId
 */
OrderRegulatedInfo.prototype.amazonOrderId = undefined

/**
 * @member {module:orders_v0/model/RegulatedInformation} regulatedInformation
 */
OrderRegulatedInfo.prototype.regulatedInformation = undefined

/**
 * When true, the order requires attaching a dosage information label when shipped.
 * @member {Boolean} requiresDosageLabel
 */
OrderRegulatedInfo.prototype.requiresDosageLabel = undefined

/**
 * @member {module:orders_v0/model/RegulatedOrderVerificationStatus} regulatedOrderVerificationStatus
 */
OrderRegulatedInfo.prototype.regulatedOrderVerificationStatus = undefined
