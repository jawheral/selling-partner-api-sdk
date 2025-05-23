/**
 * Selling Partner API for Feeds
 * The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.
 *
 * The version of the OpenAPI document: 2021-06-30
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'
import { CreateFeedDocumentResponse } from '../model/CreateFeedDocumentResponse.js'
import { CreateFeedDocumentSpecification } from '../model/CreateFeedDocumentSpecification.js'
import { CreateFeedResponse } from '../model/CreateFeedResponse.js'
import { CreateFeedSpecification } from '../model/CreateFeedSpecification.js'
import { ErrorList } from '../model/ErrorList.js'
import { Feed } from '../model/Feed.js'
import { FeedDocument } from '../model/FeedDocument.js'
import { GetFeedsResponse } from '../model/GetFeedsResponse.js'
import { SuperagentRateLimiter } from '../../../helper/SuperagentRateLimiter.mjs'
import { DefaultRateLimitFetcher } from '../../../helper/DefaultRateLimitFetcher.mjs'

/**
* Feeds service.
* @module feeds_v2021_06_30/api/FeedsApi
* @version 2021-06-30
*/
export class FeedsApi {
  // Private memeber stores the default rate limiters
  #defaultRateLimiterMap

  /**
    * Constructs a new FeedsApi.
    * @alias module:feeds_v2021_06_30/api/FeedsApi
    * @class
    * @param {module:feeds_v2021_06_30/ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:feeds_v2021_06_30/ApiClient#instance} if unspecified.
    */
  constructor (apiClient) {
    this.apiClient = apiClient || ApiClient.instance
    this.initializeDefaultRateLimiterMap()
  }

  /**
     * Initialize rate limiters for API operations
     */
  initializeDefaultRateLimiterMap () {
    this.#defaultRateLimiterMap = new Map()
    const defaultRateLimitFetcher = new DefaultRateLimitFetcher()
    const operations = [
      'FeedsApi-cancelFeed',
      'FeedsApi-createFeed',
      'FeedsApi-createFeedDocument',
      'FeedsApi-getFeed',
      'FeedsApi-getFeedDocument',
      'FeedsApi-getFeeds'
    ]

    for (const operation of operations) {
      const config = defaultRateLimitFetcher.getLimit(operation)
      this.#defaultRateLimiterMap.set(operation, new SuperagentRateLimiter(config))
    }
  }

  /**
     * Get rate limiter for a specific operation
     * @param {String} operation name
     */
  getRateLimiter (operation) {
    return this.#defaultRateLimiterMap.get(operation)
  }

  /**
     * Cancels the feed that you specify. Only feeds with &#x60;processingStatus&#x3D;IN_QUEUE&#x60; can be cancelled. Cancelled feeds are returned in subsequent calls to the [&#x60;getFeed&#x60;](https://developer-docs.amazon.com/sp-api/docs/feeds-api-v2021-06-30-reference#getfeed) and [&#x60;getFeeds&#x60;](https://developer-docs.amazon.com/sp-api/docs/feeds-api-v2021-06-30-reference#getfeeds) operations.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 15 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @param {String} feedId The identifier for the feed. This identifier is unique only in combination with a seller ID.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing HTTP response
     */
  cancelFeedWithHttpInfo (feedId) {
    const postBody = null

    // verify the required parameter 'feedId' is set
    if (feedId === undefined || feedId === null) {
      throw new Error("Missing the required parameter 'feedId' when calling cancelFeed")
    }

    const pathParams = {
      feedId
    }
    const queryParams = {
    }
    const headerParams = {
    }
    const formParams = {
    }

    const contentTypes = []
    const accepts = ['application/json']
    const returnType = null

    return this.apiClient.callApi('FeedsApi-cancelFeed',
      '/feeds/2021-06-30/feeds/{feedId}', 'DELETE',
      pathParams, queryParams, headerParams, formParams, postBody,
      contentTypes, accepts, returnType, this.getRateLimiter('FeedsApi-cancelFeed')
    )
  }

  /**
     * Cancels the feed that you specify. Only feeds with &#x60;processingStatus&#x3D;IN_QUEUE&#x60; can be cancelled. Cancelled feeds are returned in subsequent calls to the [&#x60;getFeed&#x60;](https://developer-docs.amazon.com/sp-api/docs/feeds-api-v2021-06-30-reference#getfeed) and [&#x60;getFeeds&#x60;](https://developer-docs.amazon.com/sp-api/docs/feeds-api-v2021-06-30-reference#getfeeds) operations.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 15 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @param {String} feedId The identifier for the feed. This identifier is unique only in combination with a seller ID.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}
     */
  cancelFeed (feedId) {
    return this.cancelFeedWithHttpInfo(feedId)
      .then(function (response_and_data) {
        return response_and_data.data
      })
  }

  /**
     * Creates a feed. Upload the contents of the feed document before calling this operation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0083 | 15 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).  The rate limit for the [&#x60;JSON_LISTINGS_FEED&#x60;](https://developer-docs.amazon.com/sp-api/docs/listings-feed-type-values#listings-feed) feed type differs from the rate limit for the [&#x60;createFeed&#x60;](https://developer-docs.amazon.com/sp-api/docs/feeds-api-v2021-06-30-reference#post-feeds2021-06-30feeds) operation. For more information, refer to the [Building Listings Management Workflows Guide](https://developer-docs.amazon.com/sp-api/docs/building-listings-management-workflows-guide#should-i-submit-in-bulk-using-the-json_listings_feed-or-individually-with-the-listings-items-api).
     * @param {module:feeds_v2021_06_30/model/CreateFeedSpecification} body Information required to create the feed.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link module:feeds_v2021_06_30/model/CreateFeedResponse} and HTTP response
     */
  createFeedWithHttpInfo (body) {
    const postBody = body

    // verify the required parameter 'body' is set
    if (body === undefined || body === null) {
      throw new Error("Missing the required parameter 'body' when calling createFeed")
    }

    const pathParams = {
    }
    const queryParams = {
    }
    const headerParams = {
    }
    const formParams = {
    }

    const contentTypes = ['application/json']
    const accepts = ['application/json']
    const returnType = CreateFeedResponse

    return this.apiClient.callApi('FeedsApi-createFeed',
      '/feeds/2021-06-30/feeds', 'POST',
      pathParams, queryParams, headerParams, formParams, postBody,
      contentTypes, accepts, returnType, this.getRateLimiter('FeedsApi-createFeed')
    )
  }

  /**
     * Creates a feed. Upload the contents of the feed document before calling this operation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0083 | 15 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).  The rate limit for the [&#x60;JSON_LISTINGS_FEED&#x60;](https://developer-docs.amazon.com/sp-api/docs/listings-feed-type-values#listings-feed) feed type differs from the rate limit for the [&#x60;createFeed&#x60;](https://developer-docs.amazon.com/sp-api/docs/feeds-api-v2021-06-30-reference#post-feeds2021-06-30feeds) operation. For more information, refer to the [Building Listings Management Workflows Guide](https://developer-docs.amazon.com/sp-api/docs/building-listings-management-workflows-guide#should-i-submit-in-bulk-using-the-json_listings_feed-or-individually-with-the-listings-items-api).
     * @param {module:feeds_v2021_06_30/model/CreateFeedSpecification} body Information required to create the feed.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link module:feeds_v2021_06_30/model/CreateFeedResponse}
     */
  createFeed (body) {
    return this.createFeedWithHttpInfo(body)
      .then(function (response_and_data) {
        return response_and_data.data
      })
  }

  /**
     * Creates a feed document for the feed type that you specify. This operation returns a presigned URL for uploading the feed document contents. It also returns a &#x60;feedDocumentId&#x60; value that you can pass in with a subsequent call to the [&#x60;createFeed&#x60;](https://developer-docs.amazon.com/sp-api/docs/feeds-api-v2021-06-30-reference#createfeed) operation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.5 | 15 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @param {module:feeds_v2021_06_30/model/CreateFeedDocumentSpecification} body Specifies the content type for the createFeedDocument operation.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link module:feeds_v2021_06_30/model/CreateFeedDocumentResponse} and HTTP response
     */
  createFeedDocumentWithHttpInfo (body) {
    const postBody = body

    // verify the required parameter 'body' is set
    if (body === undefined || body === null) {
      throw new Error("Missing the required parameter 'body' when calling createFeedDocument")
    }

    const pathParams = {
    }
    const queryParams = {
    }
    const headerParams = {
    }
    const formParams = {
    }

    const contentTypes = ['application/json']
    const accepts = ['application/json']
    const returnType = CreateFeedDocumentResponse

    return this.apiClient.callApi('FeedsApi-createFeedDocument',
      '/feeds/2021-06-30/documents', 'POST',
      pathParams, queryParams, headerParams, formParams, postBody,
      contentTypes, accepts, returnType, this.getRateLimiter('FeedsApi-createFeedDocument')
    )
  }

  /**
     * Creates a feed document for the feed type that you specify. This operation returns a presigned URL for uploading the feed document contents. It also returns a &#x60;feedDocumentId&#x60; value that you can pass in with a subsequent call to the [&#x60;createFeed&#x60;](https://developer-docs.amazon.com/sp-api/docs/feeds-api-v2021-06-30-reference#createfeed) operation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.5 | 15 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @param {module:feeds_v2021_06_30/model/CreateFeedDocumentSpecification} body Specifies the content type for the createFeedDocument operation.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link module:feeds_v2021_06_30/model/CreateFeedDocumentResponse}
     */
  createFeedDocument (body) {
    return this.createFeedDocumentWithHttpInfo(body)
      .then(function (response_and_data) {
        return response_and_data.data
      })
  }

  /**
     * Returns feed details (including the &#x60;resultDocumentId&#x60;, if available) for the feed that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 15 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @param {String} feedId The identifier for the feed. This identifier is unique only in combination with a seller ID.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link module:feeds_v2021_06_30/model/Feed} and HTTP response
     */
  getFeedWithHttpInfo (feedId) {
    const postBody = null

    // verify the required parameter 'feedId' is set
    if (feedId === undefined || feedId === null) {
      throw new Error("Missing the required parameter 'feedId' when calling getFeed")
    }

    const pathParams = {
      feedId
    }
    const queryParams = {
    }
    const headerParams = {
    }
    const formParams = {
    }

    const contentTypes = []
    const accepts = ['application/json']
    const returnType = Feed

    return this.apiClient.callApi('FeedsApi-getFeed',
      '/feeds/2021-06-30/feeds/{feedId}', 'GET',
      pathParams, queryParams, headerParams, formParams, postBody,
      contentTypes, accepts, returnType, this.getRateLimiter('FeedsApi-getFeed')
    )
  }

  /**
     * Returns feed details (including the &#x60;resultDocumentId&#x60;, if available) for the feed that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 15 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @param {String} feedId The identifier for the feed. This identifier is unique only in combination with a seller ID.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link module:feeds_v2021_06_30/model/Feed}
     */
  getFeed (feedId) {
    return this.getFeedWithHttpInfo(feedId)
      .then(function (response_and_data) {
        return response_and_data.data
      })
  }

  /**
     * Returns the information required for retrieving a feed document&#39;s contents.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0222 | 10 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @param {String} feedDocumentId The identifier of the feed document.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link module:feeds_v2021_06_30/model/FeedDocument} and HTTP response
     */
  getFeedDocumentWithHttpInfo (feedDocumentId) {
    const postBody = null

    // verify the required parameter 'feedDocumentId' is set
    if (feedDocumentId === undefined || feedDocumentId === null) {
      throw new Error("Missing the required parameter 'feedDocumentId' when calling getFeedDocument")
    }

    const pathParams = {
      feedDocumentId
    }
    const queryParams = {
    }
    const headerParams = {
    }
    const formParams = {
    }

    const contentTypes = []
    const accepts = ['application/json']
    const returnType = FeedDocument

    return this.apiClient.callApi('FeedsApi-getFeedDocument',
      '/feeds/2021-06-30/documents/{feedDocumentId}', 'GET',
      pathParams, queryParams, headerParams, formParams, postBody,
      contentTypes, accepts, returnType, this.getRateLimiter('FeedsApi-getFeedDocument')
    )
  }

  /**
     * Returns the information required for retrieving a feed document&#39;s contents.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0222 | 10 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @param {String} feedDocumentId The identifier of the feed document.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link module:feeds_v2021_06_30/model/FeedDocument}
     */
  getFeedDocument (feedDocumentId) {
    return this.getFeedDocumentWithHttpInfo(feedDocumentId)
      .then(function (response_and_data) {
        return response_and_data.data
      })
  }

  /**
     * Returns feed details for the feeds that match the filters that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0222 | 10 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} opts.feedTypes A list of feed types used to filter feeds. When feedTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either feedTypes or nextToken is required.
     * @param {Array.<String>} opts.marketplaceIds A list of marketplace identifiers used to filter feeds. The feeds returned will match at least one of the marketplaces that you specify.
     * @param {Number} opts.pageSize The maximum number of feeds to return in a single call. (default to 10)
     * @param {Array.<module:feeds_v2021_06_30/model/String>} opts.processingStatuses A list of processing statuses used to filter feeds.
     * @param {Date} opts.createdSince The earliest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is 90 days ago. Feeds are retained for a maximum of 90 days.
     * @param {Date} opts.createdUntil The latest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is now.
     * @param {String} opts.nextToken A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getFeeds operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link module:feeds_v2021_06_30/model/GetFeedsResponse} and HTTP response
     */
  getFeedsWithHttpInfo (opts) {
    opts = opts || {}
    const postBody = null

    const pathParams = {
    }
    const queryParams = {
      feedTypes: this.apiClient.buildCollectionParam(opts.feedTypes, 'csv'),
      marketplaceIds: this.apiClient.buildCollectionParam(opts.marketplaceIds, 'csv'),
      pageSize: opts.pageSize,
      processingStatuses: this.apiClient.buildCollectionParam(opts.processingStatuses, 'csv'),
      createdSince: opts.createdSince,
      createdUntil: opts.createdUntil,
      nextToken: opts.nextToken
    }
    const headerParams = {
    }
    const formParams = {
    }

    const contentTypes = []
    const accepts = ['application/json']
    const returnType = GetFeedsResponse

    return this.apiClient.callApi('FeedsApi-getFeeds',
      '/feeds/2021-06-30/feeds', 'GET',
      pathParams, queryParams, headerParams, formParams, postBody,
      contentTypes, accepts, returnType, this.getRateLimiter('FeedsApi-getFeeds')
    )
  }

  /**
     * Returns feed details for the feeds that match the filters that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0222 | 10 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} opts.feedTypes A list of feed types used to filter feeds. When feedTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either feedTypes or nextToken is required.
     * @param {Array.<String>} opts.marketplaceIds A list of marketplace identifiers used to filter feeds. The feeds returned will match at least one of the marketplaces that you specify.
     * @param {Number} opts.pageSize The maximum number of feeds to return in a single call. (default to 10)
     * @param {Array.<module:feeds_v2021_06_30/model/String>} opts.processingStatuses A list of processing statuses used to filter feeds.
     * @param {Date} opts.createdSince The earliest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is 90 days ago. Feeds are retained for a maximum of 90 days.
     * @param {Date} opts.createdUntil The latest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is now.
     * @param {String} opts.nextToken A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getFeeds operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link module:feeds_v2021_06_30/model/GetFeedsResponse}
     */
  getFeeds (opts) {
    return this.getFeedsWithHttpInfo(opts)
      .then(function (response_and_data) {
        return response_and_data.data
      })
  }
}
