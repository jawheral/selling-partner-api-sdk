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
import { FeatureSettings } from './FeatureSettings.js'
import { Fee } from './Fee.js'
import { FulfillmentPreviewShipment } from './FulfillmentPreviewShipment.js'
import { ScheduledDeliveryInfo } from './ScheduledDeliveryInfo.js'
import { ShippingSpeedCategory } from './ShippingSpeedCategory.js'
import { UnfulfillablePreviewItem } from './UnfulfillablePreviewItem.js'
import { Weight } from './Weight.js'

/**
 * The FulfillmentPreview model module.
 * @module fulfillmentoutbound_v2020_07_01/model/FulfillmentPreview
 * @version 2020-07-01
 */
export class FulfillmentPreview {
  /**
   * Constructs a new <code>FulfillmentPreview</code>.
   * Information about a fulfillment order preview, including delivery and fee information based on shipping method.
   * @alias module:fulfillmentoutbound_v2020_07_01/model/FulfillmentPreview
   * @class
   * @param shippingSpeedCategory {module:fulfillmentoutbound_v2020_07_01/model/ShippingSpeedCategory}
   * @param isFulfillable {Boolean} When true, this fulfillment order preview is fulfillable.
   * @param isCODCapable {Boolean} When true, this fulfillment order preview is for COD (Cash On Delivery).
   * @param marketplaceId {String} The marketplace the fulfillment order is placed against.
   */
  constructor (shippingSpeedCategory, isFulfillable, isCODCapable, marketplaceId) {
    this.shippingSpeedCategory = shippingSpeedCategory
    this.isFulfillable = isFulfillable
    this.isCODCapable = isCODCapable
    this.marketplaceId = marketplaceId
  }

  /**
   * Constructs a <code>FulfillmentPreview</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:fulfillmentoutbound_v2020_07_01/model/FulfillmentPreview} obj Optional instance to populate.
   * @return {module:fulfillmentoutbound_v2020_07_01/model/FulfillmentPreview} The populated <code>FulfillmentPreview</code> instance.
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
      obj = obj || new FulfillmentPreview()
      if (data.hasOwnProperty('shippingSpeedCategory')) { obj.shippingSpeedCategory = ShippingSpeedCategory.constructFromObject(data.shippingSpeedCategory) }
      if (data.hasOwnProperty('scheduledDeliveryInfo')) { obj.scheduledDeliveryInfo = ScheduledDeliveryInfo.constructFromObject(data.scheduledDeliveryInfo) }
      if (data.hasOwnProperty('isFulfillable')) { obj.isFulfillable = ApiClient.convertToType(data.isFulfillable, 'Boolean') }
      if (data.hasOwnProperty('isCODCapable')) { obj.isCODCapable = ApiClient.convertToType(data.isCODCapable, 'Boolean') }
      if (data.hasOwnProperty('estimatedShippingWeight')) { obj.estimatedShippingWeight = Weight.constructFromObject(data.estimatedShippingWeight) }
      if (data.hasOwnProperty('estimatedFees')) { obj.estimatedFees = ApiClient.convertToType(data.estimatedFees, [Fee]) }
      if (data.hasOwnProperty('fulfillmentPreviewShipments')) { obj.fulfillmentPreviewShipments = ApiClient.convertToType(data.fulfillmentPreviewShipments, [FulfillmentPreviewShipment]) }
      if (data.hasOwnProperty('unfulfillablePreviewItems')) { obj.unfulfillablePreviewItems = ApiClient.convertToType(data.unfulfillablePreviewItems, [UnfulfillablePreviewItem]) }
      if (data.hasOwnProperty('orderUnfulfillableReasons')) { obj.orderUnfulfillableReasons = ApiClient.convertToType(data.orderUnfulfillableReasons, ['String']) }
      if (data.hasOwnProperty('marketplaceId')) { obj.marketplaceId = ApiClient.convertToType(data.marketplaceId, 'String') }
      if (data.hasOwnProperty('featureConstraints')) { obj.featureConstraints = ApiClient.convertToType(data.featureConstraints, [FeatureSettings]) }
    }
    return obj
  }
}

/**
 * @member {module:fulfillmentoutbound_v2020_07_01/model/ShippingSpeedCategory} shippingSpeedCategory
 */
FulfillmentPreview.prototype.shippingSpeedCategory = undefined

/**
 * @member {module:fulfillmentoutbound_v2020_07_01/model/ScheduledDeliveryInfo} scheduledDeliveryInfo
 */
FulfillmentPreview.prototype.scheduledDeliveryInfo = undefined

/**
 * When true, this fulfillment order preview is fulfillable.
 * @member {Boolean} isFulfillable
 */
FulfillmentPreview.prototype.isFulfillable = undefined

/**
 * When true, this fulfillment order preview is for COD (Cash On Delivery).
 * @member {Boolean} isCODCapable
 */
FulfillmentPreview.prototype.isCODCapable = undefined

/**
 * @member {module:fulfillmentoutbound_v2020_07_01/model/Weight} estimatedShippingWeight
 */
FulfillmentPreview.prototype.estimatedShippingWeight = undefined

/**
 * An array of fee type and cost pairs.
 * @member {Array.<module:fulfillmentoutbound_v2020_07_01/model/Fee>} estimatedFees
 */
FulfillmentPreview.prototype.estimatedFees = undefined

/**
 * An array of fulfillment preview shipment information.
 * @member {Array.<module:fulfillmentoutbound_v2020_07_01/model/FulfillmentPreviewShipment>} fulfillmentPreviewShipments
 */
FulfillmentPreview.prototype.fulfillmentPreviewShipments = undefined

/**
 * An array of unfulfillable preview item information.
 * @member {Array.<module:fulfillmentoutbound_v2020_07_01/model/UnfulfillablePreviewItem>} unfulfillablePreviewItems
 */
FulfillmentPreview.prototype.unfulfillablePreviewItems = undefined

/**
 * String list
 * @member {Array.<String>} orderUnfulfillableReasons
 */
FulfillmentPreview.prototype.orderUnfulfillableReasons = undefined

/**
 * The marketplace the fulfillment order is placed against.
 * @member {String} marketplaceId
 */
FulfillmentPreview.prototype.marketplaceId = undefined

/**
 * A list of features and their fulfillment policies to apply to the order.
 * @member {Array.<module:fulfillmentoutbound_v2020_07_01/model/FeatureSettings>} featureConstraints
 */
FulfillmentPreview.prototype.featureConstraints = undefined
