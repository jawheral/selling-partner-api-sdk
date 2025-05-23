/**
 * Selling Partner API for Pricing
 * The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer information for Amazon Marketplace products.
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
import { MoneyType } from './MoneyType.js'
import { OfferCustomerType } from './OfferCustomerType.js'
import { PriceType } from './PriceType.js'
import { QuantityDiscountPriceType } from './QuantityDiscountPriceType.js'

/**
 * The OfferType model module.
 * @module pricing_v0/model/OfferType
 * @version v0
 */
export class OfferType {
  /**
   * Constructs a new <code>OfferType</code>.
   * Schema for an individual offer.
   * @alias module:pricing_v0/model/OfferType
   * @class
   * @param buyingPrice {module:pricing_v0/model/PriceType}
   * @param regularPrice {module:pricing_v0/model/MoneyType}
   * @param fulfillmentChannel {String} The fulfillment channel for the offer listing. Possible values:  * Amazon - Fulfilled by Amazon. * Merchant - Fulfilled by the seller.
   * @param itemCondition {String} The item condition for the offer listing. Possible values: New, Used, Collectible, Refurbished, or Club.
   * @param itemSubCondition {String} The item subcondition for the offer listing. Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
   * @param sellerSKU {String} The seller stock keeping unit (SKU) of the item.
   */
  constructor (buyingPrice, regularPrice, fulfillmentChannel, itemCondition, itemSubCondition, sellerSKU) {
    this.buyingPrice = buyingPrice
    this.regularPrice = regularPrice
    this.fulfillmentChannel = fulfillmentChannel
    this.itemCondition = itemCondition
    this.itemSubCondition = itemSubCondition
    this.sellerSKU = sellerSKU
  }

  /**
   * Constructs a <code>OfferType</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:pricing_v0/model/OfferType} obj Optional instance to populate.
   * @return {module:pricing_v0/model/OfferType} The populated <code>OfferType</code> instance.
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
      obj = obj || new OfferType()
      if (data.hasOwnProperty('offerType')) { obj.offerType = OfferCustomerType.constructFromObject(data.offerType) }
      if (data.hasOwnProperty('BuyingPrice')) { obj.buyingPrice = PriceType.constructFromObject(data.BuyingPrice) }
      if (data.hasOwnProperty('RegularPrice')) { obj.regularPrice = MoneyType.constructFromObject(data.RegularPrice) }
      if (data.hasOwnProperty('businessPrice')) { obj.businessPrice = MoneyType.constructFromObject(data.businessPrice) }
      if (data.hasOwnProperty('quantityDiscountPrices')) { obj.quantityDiscountPrices = ApiClient.convertToType(data.quantityDiscountPrices, [QuantityDiscountPriceType]) }
      if (data.hasOwnProperty('FulfillmentChannel')) { obj.fulfillmentChannel = ApiClient.convertToType(data.FulfillmentChannel, 'String') }
      if (data.hasOwnProperty('ItemCondition')) { obj.itemCondition = ApiClient.convertToType(data.ItemCondition, 'String') }
      if (data.hasOwnProperty('ItemSubCondition')) { obj.itemSubCondition = ApiClient.convertToType(data.ItemSubCondition, 'String') }
      if (data.hasOwnProperty('SellerSKU')) { obj.sellerSKU = ApiClient.convertToType(data.SellerSKU, 'String') }
    }
    return obj
  }
}

/**
 * @member {module:pricing_v0/model/OfferCustomerType} offerType
 */
OfferType.prototype.offerType = undefined

/**
 * @member {module:pricing_v0/model/PriceType} buyingPrice
 */
OfferType.prototype.buyingPrice = undefined

/**
 * @member {module:pricing_v0/model/MoneyType} regularPrice
 */
OfferType.prototype.regularPrice = undefined

/**
 * @member {module:pricing_v0/model/MoneyType} businessPrice
 */
OfferType.prototype.businessPrice = undefined

/**
 * List of `QuantityDiscountPrice` that contains item's pricing information when buy in bulk.
 * @member {Array.<module:pricing_v0/model/QuantityDiscountPriceType>} quantityDiscountPrices
 */
OfferType.prototype.quantityDiscountPrices = undefined

/**
 * The fulfillment channel for the offer listing. Possible values:  * Amazon - Fulfilled by Amazon. * Merchant - Fulfilled by the seller.
 * @member {String} fulfillmentChannel
 */
OfferType.prototype.fulfillmentChannel = undefined

/**
 * The item condition for the offer listing. Possible values: New, Used, Collectible, Refurbished, or Club.
 * @member {String} itemCondition
 */
OfferType.prototype.itemCondition = undefined

/**
 * The item subcondition for the offer listing. Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
 * @member {String} itemSubCondition
 */
OfferType.prototype.itemSubCondition = undefined

/**
 * The seller stock keeping unit (SKU) of the item.
 * @member {String} sellerSKU
 */
OfferType.prototype.sellerSKU = undefined
