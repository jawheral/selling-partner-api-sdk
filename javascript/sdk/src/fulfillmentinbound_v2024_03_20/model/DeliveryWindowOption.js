/**
 * The Selling Partner API for FBA inbound operations.
 * The Selling Partner API for Fulfillment By Amazon (FBA) Inbound. The FBA Inbound API enables building inbound workflows to create, manage, and send shipments into Amazon's fulfillment network. The API has interoperability with the Send-to-Amazon user interface.
 *
 * The version of the OpenAPI document: 2024-03-20
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'

/**
 * The DeliveryWindowOption model module.
 * @module fulfillmentinbound_v2024_03_20/model/DeliveryWindowOption
 * @version 2024-03-20
 */
export class DeliveryWindowOption {
  /**
   * Constructs a new <code>DeliveryWindowOption</code>.
   * Contains information pertaining to a delivery window option.
   * @alias module:fulfillmentinbound_v2024_03_20/model/DeliveryWindowOption
   * @class
   * @param availabilityType {String} Identifies type of Delivery Window Availability. Values: `AVAILABLE`, `CONGESTED`
   * @param deliveryWindowOptionId {String} Identifier of a delivery window option. A delivery window option represent one option for when a shipment is expected to be delivered.
   * @param endDate {Date} The time at which this delivery window option ends. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mmZ`.
   * @param startDate {Date} The time at which this delivery window option starts. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mmZ`.
   * @param validUntil {Date} The time at which this window delivery option is no longer valid. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mmZ`.
   */
  constructor (availabilityType, deliveryWindowOptionId, endDate, startDate, validUntil) {
    this.availabilityType = availabilityType
    this.deliveryWindowOptionId = deliveryWindowOptionId
    this.endDate = endDate
    this.startDate = startDate
    this.validUntil = validUntil
  }

  /**
   * Constructs a <code>DeliveryWindowOption</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:fulfillmentinbound_v2024_03_20/model/DeliveryWindowOption} obj Optional instance to populate.
   * @return {module:fulfillmentinbound_v2024_03_20/model/DeliveryWindowOption} The populated <code>DeliveryWindowOption</code> instance.
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
      obj = obj || new DeliveryWindowOption()
      if (data.hasOwnProperty('availabilityType')) { obj.availabilityType = ApiClient.convertToType(data.availabilityType, 'String') }
      if (data.hasOwnProperty('deliveryWindowOptionId')) { obj.deliveryWindowOptionId = ApiClient.convertToType(data.deliveryWindowOptionId, 'String') }
      if (data.hasOwnProperty('endDate')) { obj.endDate = ApiClient.convertToType(data.endDate, 'Date') }
      if (data.hasOwnProperty('startDate')) { obj.startDate = ApiClient.convertToType(data.startDate, 'Date') }
      if (data.hasOwnProperty('validUntil')) { obj.validUntil = ApiClient.convertToType(data.validUntil, 'Date') }
    }
    return obj
  }
}

/**
 * Identifies type of Delivery Window Availability. Values: `AVAILABLE`, `CONGESTED`
 * @member {String} availabilityType
 */
DeliveryWindowOption.prototype.availabilityType = undefined

/**
 * Identifier of a delivery window option. A delivery window option represent one option for when a shipment is expected to be delivered.
 * @member {String} deliveryWindowOptionId
 */
DeliveryWindowOption.prototype.deliveryWindowOptionId = undefined

/**
 * The time at which this delivery window option ends. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mmZ`.
 * @member {Date} endDate
 */
DeliveryWindowOption.prototype.endDate = undefined

/**
 * The time at which this delivery window option starts. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mmZ`.
 * @member {Date} startDate
 */
DeliveryWindowOption.prototype.startDate = undefined

/**
 * The time at which this window delivery option is no longer valid. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mmZ`.
 * @member {Date} validUntil
 */
DeliveryWindowOption.prototype.validUntil = undefined
