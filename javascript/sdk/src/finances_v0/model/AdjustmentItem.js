/**
 * Selling Partner API for Finances
 * The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order, financial event group, or date range without having to wait until a statement period closes. You can also obtain financial event groups for a given date range.
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
import { Currency } from './Currency.js'

/**
 * The AdjustmentItem model module.
 * @module finances_v0/model/AdjustmentItem
 * @version v0
 */
export class AdjustmentItem {
  /**
   * Constructs a new <code>AdjustmentItem</code>.
   * An item in an adjustment to the seller&#39;s account.
   * @alias module:finances_v0/model/AdjustmentItem
   * @class
   */
  constructor () {
  }

  /**
   * Constructs a <code>AdjustmentItem</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:finances_v0/model/AdjustmentItem} obj Optional instance to populate.
   * @return {module:finances_v0/model/AdjustmentItem} The populated <code>AdjustmentItem</code> instance.
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
      obj = obj || new AdjustmentItem()
      if (data.hasOwnProperty('Quantity')) { obj.quantity = ApiClient.convertToType(data.Quantity, 'String') }
      if (data.hasOwnProperty('PerUnitAmount')) { obj.perUnitAmount = Currency.constructFromObject(data.PerUnitAmount) }
      if (data.hasOwnProperty('TotalAmount')) { obj.totalAmount = Currency.constructFromObject(data.TotalAmount) }
      if (data.hasOwnProperty('SellerSKU')) { obj.sellerSKU = ApiClient.convertToType(data.SellerSKU, 'String') }
      if (data.hasOwnProperty('FnSKU')) { obj.fnSKU = ApiClient.convertToType(data.FnSKU, 'String') }
      if (data.hasOwnProperty('ProductDescription')) { obj.productDescription = ApiClient.convertToType(data.ProductDescription, 'String') }
      if (data.hasOwnProperty('ASIN')) { obj.ASIN = ApiClient.convertToType(data.ASIN, 'String') }
      if (data.hasOwnProperty('TransactionNumber')) { obj.transactionNumber = ApiClient.convertToType(data.TransactionNumber, 'String') }
    }
    return obj
  }
}

/**
 * Represents the number of units in the seller's inventory when the AdustmentType is FBAInventoryReimbursement.
 * @member {String} quantity
 */
AdjustmentItem.prototype.quantity = undefined

/**
 * @member {module:finances_v0/model/Currency} perUnitAmount
 */
AdjustmentItem.prototype.perUnitAmount = undefined

/**
 * @member {module:finances_v0/model/Currency} totalAmount
 */
AdjustmentItem.prototype.totalAmount = undefined

/**
 * The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.
 * @member {String} sellerSKU
 */
AdjustmentItem.prototype.sellerSKU = undefined

/**
 * A unique identifier assigned to products stored in and fulfilled from a fulfillment center.
 * @member {String} fnSKU
 */
AdjustmentItem.prototype.fnSKU = undefined

/**
 * A short description of the item.
 * @member {String} productDescription
 */
AdjustmentItem.prototype.productDescription = undefined

/**
 * The Amazon Standard Identification Number (ASIN) of the item.
 * @member {String} ASIN
 */
AdjustmentItem.prototype.ASIN = undefined

/**
 * The transaction number that is related to the adjustment.
 * @member {String} transactionNumber
 */
AdjustmentItem.prototype.transactionNumber = undefined
