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
import { Weight } from './Weight.js'

/**
 * The FulfillmentPreviewItem model module.
 * @module fulfillmentoutbound_v2020_07_01/model/FulfillmentPreviewItem
 * @version 2020-07-01
 */
export class FulfillmentPreviewItem {
  /**
   * Constructs a new <code>FulfillmentPreviewItem</code>.
   * Item information for a shipment in a fulfillment order preview.
   * @alias module:fulfillmentoutbound_v2020_07_01/model/FulfillmentPreviewItem
   * @class
   * @param sellerSku {String} The seller SKU of the item.
   * @param quantity {Number} The item quantity.
   * @param sellerFulfillmentOrderItemId {String} A fulfillment order item identifier that the seller created with a call to the `createFulfillmentOrder` operation.
   */
  constructor (sellerSku, quantity, sellerFulfillmentOrderItemId) {
    this.sellerSku = sellerSku
    this.quantity = quantity
    this.sellerFulfillmentOrderItemId = sellerFulfillmentOrderItemId
  }

  /**
   * Constructs a <code>FulfillmentPreviewItem</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:fulfillmentoutbound_v2020_07_01/model/FulfillmentPreviewItem} obj Optional instance to populate.
   * @return {module:fulfillmentoutbound_v2020_07_01/model/FulfillmentPreviewItem} The populated <code>FulfillmentPreviewItem</code> instance.
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
      obj = obj || new FulfillmentPreviewItem()
      if (data.hasOwnProperty('sellerSku')) { obj.sellerSku = ApiClient.convertToType(data.sellerSku, 'String') }
      if (data.hasOwnProperty('quantity')) { obj.quantity = ApiClient.convertToType(data.quantity, 'Number') }
      if (data.hasOwnProperty('sellerFulfillmentOrderItemId')) { obj.sellerFulfillmentOrderItemId = ApiClient.convertToType(data.sellerFulfillmentOrderItemId, 'String') }
      if (data.hasOwnProperty('estimatedShippingWeight')) { obj.estimatedShippingWeight = Weight.constructFromObject(data.estimatedShippingWeight) }
      if (data.hasOwnProperty('shippingWeightCalculationMethod')) { obj.shippingWeightCalculationMethod = ApiClient.convertToType(data.shippingWeightCalculationMethod, 'String') }
    }
    return obj
  }
}

/**
 * The seller SKU of the item.
 * @member {String} sellerSku
 */
FulfillmentPreviewItem.prototype.sellerSku = undefined

/**
 * The item quantity.
 * @member {Number} quantity
 */
FulfillmentPreviewItem.prototype.quantity = undefined

/**
 * A fulfillment order item identifier that the seller created with a call to the `createFulfillmentOrder` operation.
 * @member {String} sellerFulfillmentOrderItemId
 */
FulfillmentPreviewItem.prototype.sellerFulfillmentOrderItemId = undefined

/**
 * @member {module:fulfillmentoutbound_v2020_07_01/model/Weight} estimatedShippingWeight
 */
FulfillmentPreviewItem.prototype.estimatedShippingWeight = undefined

/**
 * Allowed values for the <code>shippingWeightCalculationMethod</code> property.
 * @enum {String}
 * @readonly
 */
FulfillmentPreviewItem.ShippingWeightCalculationMethodEnum = {

  /**
     * value: "Package"
     * @const
     */
  Package: 'Package',

  /**
     * value: "Dimensional"
     * @const
     */
  Dimensional: 'Dimensional'
}

/**
 * The method used to calculate the estimated shipping weight.
 * @member {module:fulfillmentoutbound_v2020_07_01/model/FulfillmentPreviewItem.ShippingWeightCalculationMethodEnum} shippingWeightCalculationMethod
 */
FulfillmentPreviewItem.prototype.shippingWeightCalculationMethod = undefined
